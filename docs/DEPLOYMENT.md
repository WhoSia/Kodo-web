# Deployment — Kodo-web

## Live production

- Domain: https://kodoresearch.org/
- Canonical site repository: [WhoSia/Kodo-web](https://github.com/WhoSia/Kodo-web), `main`
- Hosting: team-managed **Cloudflare** (reported by deployment owner)
- Latest confirmed source release: `v0.11.6`
- Latest production deployment commit SHA: **[verify in Cloudflare dashboard]**

## Operational release path

1. Update the source on `WhoSia/Kodo-web/main`.
2. Verify the commit and site gate.
3. Check the Cloudflare dashboard for the production deployment's commit SHA and status. Repo connectivity has been repaired according to the deployment owner, but GitHub source state alone does not prove live promotion.
4. Verify https://kodoresearch.org/ on desktop and mobile and confirm the visible release changes.
5. If the site is stale, compare Cloudflare's connected repository and production SHA to `WhoSia/Kodo-web/main` before retrying.

## Historical note

The initial handoff proposed a Vercel Git import and later encountered a separate Cloudflare-import snapshot repository. Those instructions are historical and **not** the current production runbook. This static website does not require a framework, build dependencies, environment variables, or a local development server for production consumption.

Deployment credentials, DNS records, the exact Cloudflare project name and production source binding are deliberately **[not recorded here / to confirm with owner]**.
