# Website Prototype 0.11.4 — Perception-First Research Identity

Status: **PASS — PERCEPTION FIRST / POLICY SECOND**

## Authority update

New team clarification changes the public research emphasis:

- The main research difficulty is extracting reliable game state from the live screen.
- CNN / computer vision is therefore the current research core.
- Reinforcement learning remains part of Kodo, but it is downstream of the perception/data layer.
- YOLO via Ultralytics and OpenCV remain current implementation tooling.
- Projectile tracking remains the hardest visual state currently discussed by the implementation team.

## Public narrative consequence

The homepage now reads in this order:

1. Hero — `pixels → state → policy`
2. Perception
3. System
4. Roadmap
5. Progress
6. Colt ambition

Key public phrases:

- **The hard part is seeing the game.**
- **Pixels first. Policy second.**
- **Perception creates the data layer. Learning starts once the state is reliable.**

## What is not claimed

- The site does not claim a final CNN architecture.
- It does not claim projectile state is mathematically impossible to recover.
- It does not claim reinforcement learning is trivial in general.

The public page instead expresses the team’s current engineering bottleneck: reliable screen-to-state recovery.
