# Website Prototype 0.11.7 — Visual Fidelity & Structural Consolidation

**Full name:** Cascade Simplification, Interaction Contract Repair & Evidence-Grounded Design Assurance.

## Evidence and intended limits

Initial 0.11.7 source audit: `styles.css` imported the stale `tokens.css` and seven active cascade patches `part-8` through `part-14`. Across those seven patches there were 41 occurrences of `!important`. Historic `part-1`–`part-7` were not imported. `script.js` expected `.menu-mark` absent from HTML; media-loader and figure-animation selectors had no matching elements. The old CI verified textual markers but no browser behavior.

### Changes

1. Consolidated active CSS into `styles.css` in **exact original part-8→part-14 order**, preserving all rule bodies and selector ordering. Only the orphan 0.6 brand-experiment tokens and unused `.wordmark` rules were omitted after confirming no `var(--brand-*)` references in active CSS. Added a `[hidden]` rule for the mobile nav; this is a **functional** change and must be tested.
2. Removed inactive historical CSS parts, now retained by Git history. No automated selector-level pruning was claimed, and the 41 existing `!important` declarations remain a separate optimization opportunity.
3. Repaired mobile menu DOM mark and added Escape, outside pointer, desktop breakpoint and focus restoration behavior.
4. Removed the disconnected media manifest and unreferenced figure-intersection animation path. Media admission policy remains in `docs/MEDIA_INTAKE.md`.
5. Rephrased Hero metadata `TOOLING` → `CV REFERENCE` to avoid representing external technical examples as confirmed Kodo integration.
6. Replaced the text-only site gate with structural asset/DOM/CSS contracts and added Playwright tests for three viewport widths, horizontal overflow, theme storage and responsive menu behavior.

### Verification authority

- Mechanically preserved declaration ordering: supported by source concatenation.
- Static/DOM verification: must pass `python tools/check_site.py`.
- Browser behavior: must pass `node tools/check_browser.cjs` in GitHub Actions; **the workflow result is required before claiming PASS**.
- Pixel equivalence before/after: **NOT VERIFIED**; requires archived screenshots or computed-style comparisons at matched viewports and font availability.
- Live Cloudflare deployment: **NOT VERIFIED** by GitHub source commits.
- Exact used-css selector pruning, Lighthouse, or multi-browser visual diff: **NOT PERFORMED**.

## LIRA/JEV audit scale (0–1, evaluative rather than measured)

| Gate | Prior | Target | Authority |
|---|---:|---:|---|
| CSS source traceability | 0.48 | 0.82 | Count of active imports + order audit; full dead selector cleanup pending |
| Interaction contracts | 0.55 | 0.90 | DOM, JS, Escape/outside/menu tests |
| Verification effectiveness | 0.35 | 0.80 | Browser CI runtime required |
| Visual fidelity confidence | 0.45 | 0.75 | Browser layout smoke tests only; pixel proof pending |
| Public claim calibration | 0.68 | 0.83 | CV attribution language corrected |

Scores are qualitative priors/targets, **not achieved measured post-release ratings**. A failing CI or visual regression overrides this forecast.

## Open follow-up

- Compare same-font, same-viewport screenshots from v0.11.6 and v0.11.7.
- Selectively remove stale selectors and `!important` only after computed-style evidence.
- Verify Cloudflare production commit and real domain interaction.
- Future approved Kodo detection screenshots should replace conceptual instrumentation when project evidence arrives.
