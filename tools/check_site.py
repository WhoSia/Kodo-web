from pathlib import Path
from bs4 import BeautifulSoup
root=Path(__file__).resolve().parents[1]
html=(root/'index.html').read_text(encoding='utf-8')
soup=BeautifulSoup(html,'html.parser')
forbidden_public=['KODO','PROJECT X','PufferRL','MAPPO','YOLOv8','Transformer','LSTM','132-d','138-d','MultiDiscrete','G1 ','G2 ','G3 ','G4 ','G5 ','G6 ','G7 ']
checks={
 'title': soup.title and soup.title.string=='Kodo — NPLUS',
 'brand_case': 'KODO' not in html,
 'legacy_placeholder': 'PROJECT X' not in html,
 'hero': 'Building agents' in html and 'that learn to play.' in html,
 'new_nav': all(soup.select_one(f'a[href="#{x}"]') is not None for x in ['overview','stack','roadmap','status']),
 'new_sections': all(soup.select_one(f'#{x}') is not None for x in ['overview','stack','roadmap','status']),
 'authority_labels': 'WORKING ARCHITECTURE' in html and 'WORKING ROADMAP' in html and 'CONFIRMED BUILD' in html,
 'candidate_details_withheld': not any(x in html for x in forbidden_public),
 'media_manifest': (root/'media-manifest.js').exists(),
 'media_slot': soup.select_one('[data-media-slot="hero"]') is not None,
 'constellation': soup.select_one('.hero-constellation') is not None,
 'diagram_css': (root/'styles/part-6.css').exists() and 'part-6.css' in (root/'styles.css').read_text(),
 'authority_doc': (root/'docs/ARCHITECTURE_AUTHORITY_V0_10_3.md').exists(),
 'unique_ids': len([x.get('id') for x in soup.find_all(id=True)]) == len(set(x.get('id') for x in soup.find_all(id=True))),
}
failed=[k for k,v in checks.items() if not v]
for k,v in checks.items(): print(('PASS' if v else 'FAIL'), k)
if failed: raise SystemExit('SITE_GATE=FAIL: '+', '.join(failed))
print('SITE_GATE=PASS')
