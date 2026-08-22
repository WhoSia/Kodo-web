# Website Prototype 0.10.3 — Architecture Authority Reconciliation

Status: **PUBLIC STRUCTURE REFACTORED / EXACT STACK NOT LOCKED**

## Source order

1. Latest teammate reply (2026-08-22 18:12–18:23): the architecture is **not confirmed**, but is likely to stay close to the current direction; the diagram was then simplified because the earlier version was too complex for public explanation.
2. Latest simplified Training Roadmap revision: governs the **public narrative structure**.
3. Earlier richer roadmap/stack diagrams: retained as intermediate planning evidence, but do not override the later simplification.
4. Deleted chat content: no recoverable content, therefore no claim authority.

## Authority reconciliation

### Confirmed build facts

- Team identity: NPLUS
- Project identity: Kodo
- Core game logic: implemented
- UI: implemented
- Gas system: in development
- Public member roster: intentionally omitted

### Working architecture — may be shown only with status labels

- one actor-facing contract across simulation/device observation paths;
- source → observation → representation → memory → policy → action decomposition;
- human video → CV reverse-engineering → behaviour cloning → multi-agent learning → device test roadmap;
- training-only information may differ from deployed actor information;
- device-side changes can create retraining dependencies.

### Candidate implementation details — do not render as locked homepage facts

The planning material currently contains names such as Transformer, LSTM, MAPPO, PufferRL, PPO/V-trace/GAE, YOLOv8 and minitouch. The teammate explicitly said the stack is not confirmed. These names remain **candidate / likely-direction evidence**, not final architecture authority.

### Withheld from the public homepage until confirmed

- exact observation / critic dimensions;
- action-space cardinalities;
- gamma/lambda and other hyperparameters;
- numerical aim/delay/evaluation targets;
- detailed G1–G7 or G1–G4 blocker contents;
- exact model/library names as if deployed or final.

## Revision interpretation

The later simplified roadmap is not merely a prettier version. It is an **authority mutation**: the public explanation is deliberately coarser than the internal planning artifact. The website therefore copies the diagram's information grammar, not its full internal payload.

## Homepage consequence

Retire the generic `Build / Learning / System` taxonomy and standalone Observatory as the dominant public structure.

Adopt:

`Hero → Overview → Stack → Roadmap → Status`

- **Overview** explains the current system premise.
- **Stack** visualizes roles and authority states, not exact libraries.
- **Roadmap** shows the working order of work without exposing unconfirmed blockers or metrics.
- **Status** explicitly separates confirmed build facts from working architectural direction.

## Diagram grammar

A bounded semantic palette is allowed only inside technical diagrams:

- blue — source / environment / device
- green — observation / representation / memory
- violet — policy / action
- amber — training-only path
- cyan — deploy/device path
- red — gate / blocker / invalidating dependency

Color is never the sole carrier of meaning; role labels and line semantics remain required.

## Release blocker

Any future homepage patch that publishes candidate model/library names, dimensions, action counts, hyperparameters, or blocker IDs as confirmed facts must first obtain an explicit architecture confirmation from NPLUS.
