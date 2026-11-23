"""Kodo-web static contract audit. Runtime layout/interaction lives in check_browser.cjs."""
from html.parser import HTMLParser
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
html = (ROOT / "index.html").read_text(encoding="utf-8")
css = (ROOT / "styles.css").read_text(encoding="utf-8")
js = (ROOT / "script.js").read_text(encoding="utf-8")

class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.nodes = []
        self.assets = []
    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        self.nodes.append((tag, d))
        if "id" in d:
            self.ids.append(d["id"])
        for k in ("src", "href"):
            value = d.get(k, "")
            if value.startswith("./") and not value.startswith("./#"):
                self.assets.append(value.removeprefix("./").split("#")[0].split("?")[0])

p = SiteParser()
p.feed(html)

def nodes_with(key):
    return [(tag, attrs) for tag, attrs in p.nodes if key in attrs]

menu = nodes_with("data-menu-button")
nav = nodes_with("data-mobile-nav")
toggle = nodes_with("data-theme-toggle")
def class_exists(name):
    return any(name in attrs.get("class", "").split() for _, attrs in p.nodes)

def valid_css_balance(source):
    """Skip quoted text and /* comments */ before counting CSS braces."""
    source = re.sub(r"/\*.*?\*/", "", source, flags=re.S)
    source = re.sub(r"""(?:"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*')""", "''", source)
    return source.count("{") == source.count("}")

checks = {
    "site_title_and_identity": "<title>Kodo — NPLUS</title>" in html and "Building agents" in html,
    "stable_navigation_targets": all(section in p.ids for section in ("main", "perception", "system", "roadmap", "progress", "real-world")),
    "unique_ids": len(p.ids) == len(set(p.ids)),
    "menu_dom_contract": len(menu) == len(nav) == 1 and class_exists("menu-mark")
        and menu[0][1].get("aria-controls") == "mobile-nav"
        and menu[0][1].get("aria-expanded") == "false"
        and "hidden" in nav[0][1]
        and ".menu-mark" in js
        and "Escape" in js,
    "theme_contract": len(toggle) == 1 and "data-theme" in html and "kodo-theme-v0112" in js
        and "kodo-theme-v0112" in html and "localStorage.setItem" in js,
    "all_local_assets_exist": all((ROOT / asset).is_file() for asset in p.assets),
    "consolidated_css": not re.search(r"@import\\s+url\\([^)]*part-\\d+\\.css", css)
        and "SOURCE: styles/part-13.css" in css and "SOURCE: styles/part-14.css" in css,
    "css_balanced": valid_css_balance(css),
    "media_dead_path_removed": "media-manifest.js" not in html and "data-media-slot" not in js,
    "perception_first": html.index('id="perception"') < html.index('id="system"'),
    "roadmap_stations": len(nodes_with("class")) > 0 and html.count('class="roadmap-stop ') == 5,
    "research_claim_guard": "CV REFERENCE" in html and "TOOLING</b> YOLO" not in html,
    "no_public_github_cta": "github.com/WhoSia/Kodo-web" not in html,
}
for label, ok in checks.items():
    print(f"{label}: {'PASS' if ok else 'FAIL'}")
print("SITE_CONTRACT_GATE=" + ("PASS" if all(checks.values()) else "FAIL"))
if not all(checks.values()):
    raise SystemExit(1)
