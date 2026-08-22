# Deployment handoff

## GitHub

Intended repository:

- owner: `WhoSia`
- repository: `Kodo-web`
- visibility: private initially
- default branch: `main`
- collaborator requested by NPLUS: `KR-penguin` with write access

## Vercel

The current site is a static root site with no package installation or build command.

Recommended flow:

1. Import the GitHub repository in Vercel (`Add New` → `Project`).
2. Let the repository root be the project root.
3. No environment variables are currently required.
4. Deploy and verify desktop + mobile.
5. Connect the final domain afterwards on the deployment owner's side.

The codebase intentionally avoids a framework until the site needs functionality that justifies one.
