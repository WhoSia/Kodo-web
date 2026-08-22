from pathlib import Path
from bs4 import BeautifulSoup
root=Path(__file__).resolve().parents[1]
html=(root/'index.html').read_text(encoding='utf-8')
soup=BeautifulSoup(html,'html.parser')
checks={
 'title': soup.title and soup.title.string=='Kodo — NPLUS',
 'brand_case': 'KODO' not in html,
 'legacy_placeholder': 'PROJECT X' not in html,
 'hero': 'Building agents' in html and 'that learn to play.' in html,
 'media_manifest': (root/'media-manifest.js').exists(),
 'media_slot': soup.select_one('[data-media-slot="hero"]') is not None,
 'constellation': soup.select_one('.hero-constellation') is not None,
 'unique_ids': len([x.get('id') for x in soup.find_all(id=True)]) == len(set(x.get('id') for x in soup.find_all(id=True))),
}
failed=[k for k,v in checks.items() if not v]
for k,v in checks.items(): print(('PASS' if v else 'FAIL'), k)
if failed: raise SystemExit('SITE_GATE=FAIL: '+', '.join(failed))
print('SITE_GATE=PASS')
