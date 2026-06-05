# 📊 Dashboard

> [!info] 이 페이지는 Obsidian + Dataview 플러그인에서만 렌더됩니다. raw markdown·Quartz 빌드에서는 코드블록으로 보입니다.

카테고리 catalog는 [[index]] 참조.

---

## 전체 현황

```dataviewjs
const pages = dv.pages('"wiki"');
const overviews = pages.where(p => p.file.folder.includes("overviews")).length;
dv.paragraph(`총 **${pages.length}** 편  ·  overview ${overviews}편  ·  마지막 갱신 ${dv.luxon.DateTime.now().toFormat("yyyy-MM-dd")}`);
```

## 카테고리별 (상위 폴더 기준)

```dataview
TABLE length(rows) AS "편수"
FROM "wiki"
FLATTEN regexreplace(file.folder, "wiki/([^/]+).*", "$1") AS 카테고리
GROUP BY 카테고리
SORT length(rows) DESC
```

## 근거등급별 분포 (근거 위계순)

```dataviewjs
// 근거 위계: 높음(sr+ma) → 낮음(narrative). CLAUDE.md confidence vocabulary 순서
const order = ["sr+ma","sr","rct","prospective","retrospective","cross-sectional",
               "case-report","in-vivo","animal","in-vitro","narrative-review","consensus","synthesis"];
const pages = dv.pages('"wiki"').where(p => p.confidence);
const counts = {};
for (const p of pages) {
  const c = String(p.confidence);
  counts[c] = (counts[c] || 0) + 1;
}
const known = order.filter(k => counts[k]);
const unknown = Object.keys(counts).filter(k => !order.includes(k)).sort((a, b) => counts[b] - counts[a]);
const labels = [...known, ...unknown];
const max = Math.max(...Object.values(counts));
// 색: 높은 근거=짙은 녹색 → 낮은 근거=회색조
function color(label) {
  const i = order.indexOf(label);
  if (i === -1) return "var(--text-muted)";
  const t = i / (order.length - 1);
  return `hsl(${Math.round(140 - t * 140)}, ${Math.round(55 - t * 38)}%, ${Math.round(42 + t * 16)}%)`;
}
let html = '';
for (const l of labels) {
  const c = counts[l];
  const w = Math.max(2, Math.round(c / max * 100));
  html += `<div style="display:flex;align-items:center;margin:3px 0;font-size:0.85em;">
    <span style="width:110px;text-align:right;padding-right:8px;flex:none;">${l}</span>
    <span style="height:15px;width:${w}%;background:${color(l)};border-radius:3px;flex:none;"></span>
    <span style="padding-left:6px;flex:none;">${c}</span>
  </div>`;
}
const el = dv.el("div", "");
el.innerHTML = html;
```

## 연도별 (막대그래프)

```dataviewjs
const pages = dv.pages('"wiki"').where(p => p.year);
const counts = {};
for (const p of pages) counts[p.year] = (counts[p.year] || 0) + 1;
const years = Object.keys(counts).sort((a, b) => Number(b) - Number(a));
const max = Math.max(...Object.values(counts));
// 색: 최신=선명한 청록 → 과거=옅은 회청색 (위에서 아래로 fade)
function color(idx, total) {
  const t = total > 1 ? idx / (total - 1) : 0; // 0 최신 .. 1 과거
  return `hsl(${Math.round(190 - t * 25)}, ${Math.round(65 - t * 50)}%, ${Math.round(45 + t * 22)}%)`;
}
let html = '';
years.forEach((y, idx) => {
  const c = counts[y];
  const w = Math.max(2, Math.round(c / max * 100));
  html += `<div style="display:flex;align-items:center;margin:3px 0;font-size:0.85em;">
    <span style="width:52px;text-align:right;padding-right:8px;flex:none;">${y}</span>
    <span style="height:15px;width:${w}%;background:${color(idx, years.length)};border-radius:3px;flex:none;"></span>
    <span style="padding-left:6px;flex:none;">${c}</span>
  </div>`;
});
const el = dv.el("div", "");
el.innerHTML = html;
```

## Superseded (후속 근거로 대체된 페이지)

```dataview
TABLE superseded_scope AS "범위", superseded_by AS "대체 →"
FROM "wiki"
WHERE superseded_by
SORT file.name ASC
```

## 최근 추가/수정 10편

```dataview
TABLE confidence AS "등급", file.mtime AS "수정시각"
FROM "wiki"
SORT file.mtime DESC
LIMIT 10
```
