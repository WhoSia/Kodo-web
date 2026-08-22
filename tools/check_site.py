from pathlib import Path
from bs4 import BeautifulSoup
root=Path(__file__).resolve().parents[1]
html=(root/'index.html').read_text(encoding='utf-8')
soup=BeautifulSoup(html,'html.parser')
forbidden_public=['KODO','PROJECT X','PufferRL','MAPPO','YOLOv8','Transformer','LSTM','132-d','138-d','MultiDiscrete','G1 ','G2 ','G3 ','G4 ','G5 ','G6 ','G7 ']
defensive_public=['WITHHELD','PUBLIC SIMPLIFICATION','AUTHORITY BASIS','CONCEPTUAL FALLBACK','not locked','under review','deliberately withheld']
hero=soup.select_one('#top')
checks={
 'title': soup.title and soup.title.string=='Kodo — NPLUS',
 'brand_case': 'KODO' not in html,
 'legacy_placeholder': 'PROJECT X' not in html,
 'hero': 'Building agents' in html and 'that learn to play.' in html,
 'hero_no_colt': hero is not None and 'Colt' not in hero.get_text(' ',strip=True),
 'new_nav': all(soup.select_one(f'a[href="#{x}"]') is not None for x in ['overview','stack','roadmap','progress']),
 'new_sections': all(soup.select_one(f'#{x}') is not None for x in ['overview','stack','roadmap','progress','ambition']),
 'ambition_colt': 'FIRST TARGET / COLT' in html and 'Start with Colt.' in html and 'Don’t stop there.' in html,
 'candidate_details_withheld': not any(x in html for x in forbidden_public),
 'public_tone': not any(x.lower() in html.lower() for x in defensive_public),
 'media_manifest': (root/'media-manifest.js').exists(),
 'media_slot': soup.select_one('[data-media-slot="hero"]') is not None,
 'media_label': 'SYSTEM SCHEMATIC' in html,
 'constellation': soup.select_one('.hero-constellation') is not None,
 'diagram_css': all((root/f'styles/part-{n}.css').exists() for n in [6,7]) and 'part-7.css' in (root/'styles.css').read_text(),
 'authority_doc': (root/'docs/ARCHITECTURE_AUTHORITY_V0_10_3.md').exists() and (root/'docs/TECHNICAL_NARRATIVE_V0_10_4.md').exists(),
 'unique_ids': len([x.get('id') for x in soup.find_all(id=True)]) == len(set(x.get('id') for x in soup.find_all(id=True))),
}
failed=[k for k,v in checks.items() if not v]
for k,v in checks.items(): print(('PASS' if v else 'FAIL'), k)
if failed: raise SystemExit('SITE_GATE=FAIL: '+', '.join(failed))
print('SITE_GATE=PASS')
