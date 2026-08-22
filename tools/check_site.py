from pathlib import Path
from html.parser import HTMLParser

ROOT = Path(__file__).resolve().parents[1]
html = (ROOT / 'index.html').read_text(encoding='utf-8')
styles = (ROOT / 'styles.css').read_text(encoding='utf-8')
css12 = (ROOT / 'styles' / 'part-12.css').read_text(encoding='utf-8')

class AuditParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids=[]
    def handle_starttag(self, tag, attrs):
        d=dict(attrs)
        if 'id' in d: self.ids.append(d['id'])

p=AuditParser(); p.feed(html)

banned_public = [
    'not locked','under review','withheld','public truth','public simplification',
    'authority basis','exact stack not locked','defensive','provisional'
]
required = [
    'Building agents','YOLO + OpenCV','Projectile tracking','Start with Colt.',
    'kodoresearch.org','assets/kodo-crest-v0113.webp','KODO / SYSTEM FIELD'
]
checks = {
    'kodo_case': 'Kodo' in html and '>KODO<' not in html,
    'nplus': 'NPLUS' in html,
    'required_copy': all(x in html for x in required),
    'github_public_link_removed': 'github.com/WhoSia/Kodo-web' not in html,
    'no_defensive_public_copy': not any(x.lower() in html.lower() for x in banned_public),
    'unique_ids': len(p.ids) == len(set(p.ids)),
    'brand_assets': all((ROOT / 'assets' / x).exists() for x in ['kodo-crest-v0113.webp','nplus-logo.webp']),
    'v0113_css_wired': 'styles/part-12.css' in styles,
    'square_instrument': 'aspect-ratio:1' in css12,
    'dark_first': "theme = stored === 'light' ? 'light' : 'dark'" in html,
    'responsive_css': '@media(max-width:720px)' in css12,
}
for k,v in checks.items(): print(f'{k}: {"PASS" if v else "FAIL"}')
if not all(checks.values()):
    print('AESTHETIC_SURFACE_GATE=FAIL')
    raise SystemExit(1)
print('AESTHETIC_SURFACE_GATE=PASS')
