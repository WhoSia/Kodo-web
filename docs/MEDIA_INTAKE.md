# Real media intake

The website should prefer approved, real Kodo project artifacts over decorative AI imagery. The former `media-manifest.js` was inert in the v0.11.6 DOM and was retired in v0.11.7. A new media feature must be implemented and tested when actual assets exist; editing a disconnected manifest cannot activate imagery.

## Admission gate

Only publish actual Kodo output with team approval; check for user data, credentials, private Discord screenshots and local paths; keep captions and metrics source-grounded. Third-party Brawl Stars game imagery must not imply affiliation with Supercell.

## Future hero media integration

1. Add an approved project screenshot or clip to `assets/` (for example `assets/kodo-environment.webp`).
2. Replace or complement the conceptual `hero-instrument` figure in `index.html` with a semantic `<figure>` and a descriptive `<img>` or video poster.
3. Add alt text, a source-backed caption, and the correct dimensions/aspect ratio.
4. Update `tools/check_site.py` and `tools/check_browser.cjs` to verify asset loading and responsive behavior.
5. Re-run the browser checks and compare against the previous visual baseline.

The conceptual schematic remains until an actual approved visual is provided.
