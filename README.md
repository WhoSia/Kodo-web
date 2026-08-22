# Kodo-web

Official web prototype for **Kodo**, an NPLUS project building a controllable Brawl Stars environment and training agents inside it.

## Current public truth

- Team: **NPLUS**
- Project: **Kodo** (exact case; do not render as `KODO`)
- Scope: the Brawl Stars agent project as a whole
- Core game logic: implemented
- UI: implemented
- Gas system: in development
- RL algorithm: not locked
- Computer-vision approach: not locked
- Team roster: intentionally omitted because membership/activity is expected to change

## Run locally

No build step is required.

```bash
python -m http.server 4173
```

Then open `http://localhost:4173`.

## Add real Kodo media

1. Put an approved image in `assets/`, preferably WebP.
2. Edit `media-manifest.js` and change the corresponding slot from `conceptual` to `real`.
3. Supply a truthful alt description and caption.
4. Do not label synthetic/mock media as real project output.

See [`docs/MEDIA_INTAKE.md`](docs/MEDIA_INTAKE.md).

## Deployment

This repository is intentionally dependency-free and suitable for a simple Git/Vercel import. No framework build command is required for the current version.

## Brand rule

`Kodo` is case-sensitive brand text. The team is `NPLUS`. Avoid merging them into a new formal name unless NPLUS explicitly decides to do so.

## Repository collaboration

The intended GitHub collaborator is `KR-penguin` with write access. This repository permission is separate from public team attribution on the website.

See [`docs/DEPLOYMENT.md`](docs/DEPLOYMENT.md) for the handoff settings.
