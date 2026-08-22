from pathlib import Path
from html.parser import HTMLParser

ROOT = Path(__file__).resolve().parents[1]
html = (ROOT / 'index.html').read_text(encoding='utf-8')
css = (ROOT / 'styles' / 'part-8.css').read_text(encoding='utf-8')

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
    'kodoresearch.org','assets/kodo-logo.webp','assets/nplus-logo.webp'
]
checks = {
    'kodo_case': 'Kodo' in html and '>KODO<' not in html,
    'nplus': 'NPLUS' in html,
    'required_copy': all(x in html for x in required),
    'no_defensive_public_copy': not any(x.lower() in html.lower() for x in banned_public),
    'unique_ids': len(p.ids) == len(set(p.ids)),
    'logo_assets': all((ROOT / 'assets' / x).exists() for x in ['kodo-logo.webp','nplus-logo.webp']),
    'responsive_css': '@media(max-width:720px)' in css,
    'reduced_motion': 'prefers-reduced-motion' in css,
}
for k,v in checks.items(): print(f'{k}: {"PASS" if v else "FAIL"}')
if not all(checks.values()):
    print('PUBLIC_SURFACE_GATE=FAIL')
    raise SystemExit(1)
print('PUBLIC_SURFACE_GATE=PASS')
