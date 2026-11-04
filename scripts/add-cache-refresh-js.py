#!/usr/bin/env python3
"""
기존 interactives/*.html 에 캐시 갱신 JS를 일괄 삽입한다.

삽입 위치: </head> 바로 앞
삽입 내용: 30분 이상 백그라운드 탭으로 있다가 복귀 시 hard-reload (visibilitychange).
           (인덱스 ?v= 파라미터가 메인 경로를 커버하므로 직접 접근·북마크 보완용)

멱등(idempotent): 이미 삽입된 파일은 스킵한다.
AUTO 도구(매 배포 재생성): 스킵한다.

실행: python3 scripts/add-cache-refresh-js.py [--dry-run]
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INTERACTIVES = ROOT / "interactives"
DRY_RUN = "--dry-run" in sys.argv

FM_PAT = re.compile(r"^<!--\s*\n---\n(.*?)\n---\s*\n-->", re.DOTALL)
MARKER = "/* llm-wiki cache-refresh */"

CACHE_JS_TEMPLATE = """\
<script>
/* llm-wiki cache-refresh */
(function(){{
  var HK='_cr_h_{key}';
  var THRESHOLD=30*60*1000;
  document.addEventListener('visibilitychange',function(){{
    if(document.hidden){{
      try{{localStorage.setItem(HK,Date.now());}}catch(e){{}}
    }}else{{
      try{{
        var t=parseInt(localStorage.getItem(HK)||'0');
        if(t&&(Date.now()-t)>THRESHOLD){{localStorage.setItem(HK,'0');location.reload(true);}}
      }}catch(e){{}}
    }}
  }});
}})();
</script>
"""

def get_frontmatter_fields(text: str) -> dict:
    m = FM_PAT.match(text)
    if not m:
        return {}
    import yaml
    try:
        return yaml.safe_load(m.group(1)) or {}
    except Exception:
        return {}

def process(path: Path) -> str | None:
    """Returns 'skipped', 'already', 'patched'."""
    text = path.read_text(encoding="utf-8")
    fields = get_frontmatter_fields(text)
    date_raw = str(fields.get("date", "")).strip()
    if date_raw.upper() == "AUTO":
        return "skipped-auto"
    if MARKER in text:
        return "already"
    # filename stem → safe key (alphanumeric+underscore, max 40 chars)
    key = re.sub(r"[^a-z0-9]", "_", path.stem.lower())[:40]
    js_block = CACHE_JS_TEMPLATE.format(key=key)
    if "</head>" in text:
        new_text = text.replace("</head>", js_block + "</head>", 1)
    else:
        # 헤드 없는 프래그먼트: frontmatter 닫는 --> 직후 삽입
        fm_end = text.find("-->\n")
        if fm_end == -1:
            return "skipped-no-fm-end"
        insert_pos = fm_end + len("-->\n")
        new_text = text[:insert_pos] + js_block + text[insert_pos:]
    if not DRY_RUN:
        path.write_text(new_text, encoding="utf-8")
    return "patched"

def main():
    patched = skipped_auto = already = skipped_other = 0
    for p in sorted(INTERACTIVES.glob("*.html")):
        if p.name in {"index.html", "overviews-map.html"}:
            continue
        result = process(p)
        if result == "patched":
            patched += 1
            print(f"  patched  {p.name}")
        elif result == "already":
            already += 1
        elif result == "skipped-auto":
            skipped_auto += 1
        else:
            skipped_other += 1
            print(f"  skipped  {p.name}  ({result})")
    mode = "[DRY RUN] " if DRY_RUN else ""
    print(f"\n{mode}patched={patched}  already={already}  skipped_auto={skipped_auto}  skipped_other={skipped_other}")

if __name__ == "__main__":
    main()
