# degen.md

DigitalOcean App Platform service that proxies `https://degen.md` to the [DEGEN.md](DEGEN.md) overview of crypto/DeFi agent skills, MCP servers, and CLIs.

Serves the raw DEGEN.md with ETag caching and a 5-minute browser cache. No dependencies beyond Python stdlib.

## Deploy

1. Create the app: `doctl apps create --spec .do/app.yaml`
2. Add custom domain `degen.md` in the DO App Platform dashboard
3. Configure DNS: add the CNAME record DO provides to your DigitalOcean DNS zone
4. Update the `<APP_ID>` in `.github/workflows/sync-app-spec.yml`
