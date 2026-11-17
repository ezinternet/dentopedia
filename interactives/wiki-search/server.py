#!/usr/bin/env python3
"""
Wiki Search Server — calls qmd CLI and serves the search UI.
Usage: python3 interactives/wiki-search/server.py
Then open: http://localhost:3737
"""
import json
import re
import socket
import subprocess
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

PORT = 3737
QMD_MCP_PORT = 8181
HERE = Path(__file__).parent
QMD = "qmd"


def qmd_mcp_alive() -> bool:
    """Check if qmd HTTP MCP daemon is listening on its port."""
    try:
        s = socket.create_connection(("localhost", QMD_MCP_PORT), timeout=1)
        s.close()
        return True
    except OSError:
        return False


def qmd_mcp_start() -> dict:
    """Start qmd HTTP MCP daemon. Returns {ok, message}."""
    if qmd_mcp_alive():
        return {"ok": True, "message": "already running"}
    try:
        subprocess.Popen(
            [QMD, "mcp", "--http", "--port", str(QMD_MCP_PORT), "--daemon"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        import time; time.sleep(1.5)
        if qmd_mcp_alive():
            return {"ok": True, "message": "started"}
        return {"ok": False, "message": "started but not responding yet — wait a moment"}
    except Exception as e:
        return {"ok": False, "message": str(e)}


def qmd_search(query: str, limit: int = 10, collections: list = None) -> list:
    """Run qmd search (BM25) and return structured results."""
    cmd = [QMD, "search", query, "--limit", str(limit)]

    # run from wiki root so paths are relative
    wiki_root = HERE.parent.parent

    try:
        proc = subprocess.run(
            cmd, capture_output=True, text=True, timeout=15, cwd=str(wiki_root)
        )
        raw = proc.stdout
    except Exception as e:
        return [{"error": str(e)}]

    return parse_qmd_output(raw, collections)


def parse_qmd_output(raw: str, collections: list = None) -> list:
    """Parse qmd search/query text output into structured dicts."""
    results = []
    blocks = re.split(r"\n(?=qmd://)", raw.strip())

    for block in blocks:
        if not block.strip():
            continue

        lines = block.strip().splitlines()
        if not lines:
            continue

        # first line: qmd://collection/path:line #docid
        header = lines[0]
        m = re.match(r"qmd://([^:]+):(\d+)\s+(#\S+)?", header)
        if not m:
            continue

        file = m.group(1)
        line = int(m.group(2))
        docid = m.group(3) or ""

        # collection filter
        col = file.split("/")[0] if "/" in file else file
        if collections and col not in collections:
            continue

        title = ""
        context = ""
        score = 0.0
        snippet_lines = []
        in_snippet = False

        for l in lines[1:]:
            if l.startswith("Title:"):
                title = l[6:].strip()
            elif l.startswith("Context:"):
                context = l[8:].strip()
            elif l.startswith("Score:"):
                try:
                    score = float(l[6:].strip().rstrip("%")) / 100
                except Exception:
                    pass
            elif l.startswith("@@"):
                in_snippet = True
                snippet_lines.append(l)
            elif in_snippet:
                snippet_lines.append(l)

        results.append({
            "docid": docid,
            "file": file,
            "line": line,
            "title": title or file.split("/")[-1].replace(".md", ""),
            "context": context,
            "score": score,
            "snippet": "\n".join(snippet_lines).strip(),
        })

    return results


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        pass

    def do_GET(self):
        if self.path in ("/", "/index.html"):
            body = (HERE / "index.html").read_bytes()
            self._send(200, "text/html; charset=utf-8", body)
        elif self.path == "/api/qmd-status":
            alive = qmd_mcp_alive()
            body = json.dumps({"alive": alive}).encode()
            self._send(200, "application/json", body)
        else:
            self._send(404, "text/plain", b"Not found")

    def do_POST(self):
        if self.path == "/api/qmd-start":
            result = qmd_mcp_start()
            self._send(200, "application/json", json.dumps(result).encode())
            return
        if self.path != "/api/search":
            self._send(404, "text/plain", b"Not found")
            return

        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length)

        try:
            params = json.loads(body)
            query = params.get("query", "").strip()
            limit = int(params.get("limit", 10))
            collections = params.get("collections") or None
        except Exception:
            self._send(400, "application/json", b'{"error":"bad request"}')
            return

        if not query:
            self._send(200, "application/json", b'{"results":[]}')
            return

        results = qmd_search(query, limit, collections)
        self._send(200, "application/json", json.dumps({"results": results}).encode())

    def _send(self, code: int, ctype: str, body: bytes):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", len(body))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    server = HTTPServer(("localhost", PORT), Handler)
    print(f"🦷 Wiki Search → http://localhost:{PORT}")
    print("Ctrl+C 로 종료")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n종료")
