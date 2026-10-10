# Kodo-web

The official website for **Kodo**, a project by **NPLUS**. The site presents the project's screen-to-state perception direction, game-environment development, and the path toward learning and real-time control.

**Website:** https://kodoresearch.org/

## Website status

**Current public design release:** `Website Prototype 0.11.6` — Perception-to-Field Narrative, Latency-Aware Research Direction & Editorial Release.

The site includes:
- Dark-first theme with a warm paper-style light theme and Freesentation accents
- NPLUS / Kodo brand marks
- Split Hero with a conceptual perception instrument and subtle constellation field
- Asymmetric Perception surface, editorial system flow, and five-stage Roadmap
- `FIELD CONDITIONS` section for mechanics, timing and sim-to-device transfer
- Responsive layout and reduced-motion considerations

## Project narrative and evidence

Kodo's research direction is to reconstruct game state from visual observations, develop a controlled game environment, and use the resulting representations to train agents before testing real-world control.

The last explicitly recorded Kodo build update lists core game logic and UI as implemented, with the gas system in development. A fresh build-state assessment remains **[to be confirmed]**.

External contributor/peer examples discussed by the team include:
- YOLO via Ultralytics, with v8 described for entity detection and v11 for wall detection
- OpenCV template matching, HSV masking and colour counting
- Game physics reconstruction, PPO experiments and latency simulation

These examples **do not establish that those model versions or experimental systems have been integrated into Kodo**. See [the 0.11.6 release authority record](docs/WEBSITE_V0_11_6_RELEASE.md). No unverified performance or benchmark numbers are published here.

## Production and updates

The production website is served at **https://kodoresearch.org/**. The project team reports a Cloudflare deployment connection to this GitHub repository.

- Repository source of truth: `WhoSia/Kodo-web`, branch `main`
- Website deployment: team-managed Cloudflare
- Exact production deployment SHA, build trigger, and Cloudflare configuration: **[verify in Cloudflare dashboard]**

Pushing to `main` updates the source. Confirm the latest production deployment separately when validating a release. No local server is required to *use* the live website.

## Documentation

- [0.11.6 release / technical narrative](docs/WEBSITE_V0_11_6_RELEASE.md)
- [0.11.5 aesthetic court](docs/AESTHETIC_COURT_V0_11_5.md)
- [0.11.4 research identity](docs/RESEARCH_IDENTITY_V0_11_4.md)
- [0.10.3 architecture authority](docs/ARCHITECTURE_AUTHORITY_V0_10_3.md)
- [Real-media admission gate](docs/MEDIA_INTAKE.md)

The historical website prototype genealogy is maintained in **Research OS → Kodo-web**, classified as a **Non-Lab Project**. Incomplete chronology is left explicitly open for future conversation-archive Markdown reconciliation.

Kodo is an independent NPLUS project. Brawl Stars is the target game; no affiliation with Supercell is implied.
