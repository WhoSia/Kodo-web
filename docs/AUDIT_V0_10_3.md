# Website Prototype 0.10.3 — Audit

Status: **PASS — PUBLIC STRUCTURE REFACTORED / EXACT STACK NOT LOCKED**

## Authority reconciliation

- Latest teammate reply says the architecture is not confirmed, though it is likely to remain close to the current direction.
- The later simplified Training Roadmap governs public narrative structure.
- Earlier richer stack/roadmap diagrams remain planning evidence, not final implementation authority.
- Deleted chat content carries no claim authority.

## Homepage structure

`Hero → Overview → Stack → Roadmap → Status`

- Overview: one game system, two observation paths; actor-facing contract shown as working architecture.
- Stack: source → observation → representation → memory → policy → action, without publishing exact candidate libraries/models.
- Roadmap: gate → human play video → CV reverse-engineering → behaviour cloning → multi-agent self-play → device test.
- Status: separates confirmed build facts from working direction and withheld public details.

## Public-truth gates

Confirmed and rendered:
- NPLUS / Kodo identity
- core game logic implemented
- UI implemented
- gas system in development

Working direction, labeled as such:
- simulation/device observation paths
- actor contract decomposition
- training-only vs device path separation
- human-video-to-device roadmap

Withheld from homepage until explicit confirmation:
- Transformer / LSTM / MAPPO / PufferRL / YOLOv8 / minitouch as final choices
- exact dimensions and action cardinalities
- gamma/lambda and numerical targets
- detailed G1–G7 or G1–G4 blocker content

## Local gates

`python tools/check_site.py` → `SITE_GATE=PASS`

- title: PASS
- Kodo case lock: PASS
- legacy PROJECT X absent: PASS
- hero phrase retained: PASS
- Overview / Stack / Roadmap / Status navigation: PASS
- new section IDs: PASS
- authority labels: PASS
- candidate details withheld: PASS
- media manifest + real-media slot retained: PASS
- constellation retained: PASS
- diagram CSS present: PASS
- authority document present: PASS
- duplicate IDs: none

Browser layout validation performed without screenshot generation at 1440, 820 and 390 CSS-pixel widths: no document horizontal overflow; navigation and all four new sections present.

## GitHub materialization

Repository: `WhoSia/Kodo-web` (private)

Refactor commit:
`73c46d31411dc577b2dc815cd41ba8ce695ec367`
`feat: refactor homepage around working stack and roadmap`

The remote `main` contains the new navigation, structure, `styles/part-6.css`, updated site gate, and `docs/ARCHITECTURE_AUTHORITY_V0_10_3.md`.

GitHub combined status API returned no registered statuses at audit time; this is recorded as **unreported**, not as a CI failure.
