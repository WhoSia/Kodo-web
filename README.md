# Kodo-web

Official website for **Kodo**, an **NPLUS** project reconstructing Brawl Stars state from the screen and training agents on top of that perception layer.

## Current state

- Core game logic: implemented
- UI: implemented
- Gas system: in development
- Research core: screen-to-state perception / CNN
- CV tooling: YOLO via Ultralytics + OpenCV
- Entity detection: YOLO
- Wall detection: YOLOv11 has been used
- OpenCV utilities: template matching, HSV masking, colour counting
- Perception targets: wall positions, player/ally/enemy positions, and ability-readiness signals
- Projectile tracking: current hardest visual state to recover reliably

## Live site

- https://kodoresearch.org

## Run locally

```bash
python -m http.server 4173
```

Then open `http://localhost:4173`.

## Design release v0.11.3

v0.11.3 removed the public GitHub CTA, moved the Kodo crest into the top navigation, replaced the large Hero logo with a square instrument field, strengthened dark-mode card outlines, constrained the Roadmap width, and opened the System section into a schematic.

## Research-identity release v0.11.4

v0.11.4 moves **Perception** ahead of **System**, reframes the Hero around `pixels → state`, and presents CNN / computer vision as the current research core while keeping reinforcement learning as the downstream learning layer.

See [`docs/RESEARCH_IDENTITY_V0_11_4.md`](docs/RESEARCH_IDENTITY_V0_11_4.md).
