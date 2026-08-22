from pathlib import Path
from html.parser import HTMLParser

ROOT = Path(__file__).resolve().parents[1]
html = (ROOT / 'index.html').read_text(encoding='utf-8')
styles = (ROOT / 'styles.css').read_text(encoding='utf-8')
css13 = (ROOT / 'styles' / 'part-13.css').read_text(encoding='utf-8')

class AuditParser(HTMLParser):
    def __init__(self):
        super().__init__(); self.ids=[]
    def handle_starttag(self, tag, attrs):
        d=dict(attrs)
        if 'id' in d: self.ids.append(d['id'])

p=AuditParser(); p.feed(html)

banned_public = [
    'not locked','under review','withheld','public truth','public simplification',
    'authority basis','exact stack not locked','provisional'
]
required = [
    'The hard part is seeing the game.',
    'Perception first.',
    'perception-lab',
    'roadmap-track',
    'kodo-footer-crest',
    'PROJECTILE TRACKING',
    'Start with Colt.',
    'kodoresearch.org',
]
checks = {
    'required_surface': all(x in html for x in required),
    'perception_before_system': html.index('id="perception"') < html.index('id="system"'),
    'github_cta_removed': 'github.com/WhoSia/Kodo-web' not in html,
    'no_defensive_public_copy': not any(x.lower() in html.lower() for x in banned_public),
    'unique_ids': len(p.ids) == len(set(p.ids)),
    'v0115_css_wired': 'styles/part-13.css' in styles,
    'pastel_palette': all(x in css13 for x in ['--pastel-cyan','--pastel-mint','--pastel-lavender','--pastel-peach']),
    'asymmetric_perception': 'grid-template-columns:repeat(12' in css13 and '.perception-primary{grid-column:span 7' in css13,
    'roadmap_timeline': '.roadmap-rail' in css13 and '.roadmap-stop' in css13,
    'responsive': '@media(max-width:720px)' in css13,
}
for k,v in checks.items(): print(f'{k}: {"PASS" if v else "FAIL"}')
if not all(checks.values()):
    print('AESTHETIC_SURFACE_GATE=FAIL')
    raise SystemExit(1)
print('AESTHETIC_SURFACE_GATE=PASS')
