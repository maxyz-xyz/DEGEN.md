---
name: degen
description: Registry of crypto/DeFi agent skills, MCP servers, and CLIs. Install the right tool for any onchain task.
metadata:
  author: maxyz-xyz
  version: "1.0"
---

# DEGEN.md

> The aggregated overview of crypto/DeFi skills, MCP servers, CLIs, and other agent integrations.
>
> Install this registry: `npx skills add maxyz-xyz/DEGEN.md`
>
> **Last updated:** 2025-04-03
>
> **Contributions welcome** — open a PR to add or update entries.

## Integrations

Official implementations only — no community or third-party wrappers.

| Protocol | Category | Description | Type | Install |
|----------|----------|-------------|------|---------|
| [Pendle](https://github.com/pendle-finance/pendle-ai) | DeFi | Yield trading — swap, LP, limit orders, market data | Plugin | `/plugin marketplace add pendle-finance/pendle-ai` |
| [Alchemy](https://github.com/alchemyplatform/alchemy-mcp-server) | Data | Token prices, NFTs, tx history, balances, swaps, simulations | MCP | `claude mcp add alchemy -- npx -y @alchemy/mcp-server` |
| [CoinGecko](https://github.com/coingecko/coingecko-cli) | Data | Token prices, market data, trending, OHLC, WebSocket streaming | CLI | `brew install coingecko/coingecko-cli/cg` |
| [Dune](https://github.com/duneanalytics/skills) | Data | Query blockchain data, decoded tables, saved queries | Skill | `npx skills add duneanalytics/skills` |
| [Etherscan](https://docs.etherscan.io/mcp-docs/introduction) | Data | Onchain data across 60+ EVM chains | MCP | `claude mcp add etherscan --transport http https://mcp.etherscan.io/mcp` |
| [Octav](https://github.com/Octav-Labs/octav-api-mcp) | Data | Portfolio tracking, transactions, NAV, 20+ chains | MCP | `claude mcp add octav -- npx octav-api-mcp` |
| [Chainlink](https://github.com/smartcontractkit/chainlink-agent-skills) | Infra | CRE workflows, CCIP cross-chain bridging | Skill | `npx skills add smartcontractkit/chainlink-agent-skills` |
| [Coinbase AgentKit](https://github.com/coinbase/agentkit) | Infra | Onchain wallet — swaps, transfers, staking, contract deploys | MCP | `npm i @coinbase/agentkit-model-context-protocol` |
| [Tenderly](https://docs.tenderly.co/mcp-server) | Infra | Tx simulation, debugging, tracing, Virtual TestNets | MCP | `claude mcp add tenderly --transport http https://mcp.tenderly.co/mcp` |
| [Trail of Bits](https://github.com/trailofbits/skills) | Security | 30+ security/audit plugins — smart contracts, Semgrep, YARA | Plugin | `/plugin marketplace add trailofbits/skills` |
| [AgentCash](https://agentcash.dev/skill.md) | Payments | Pay-per-call premium APIs via x402 micropayments | Skill | `npx agentcash@latest onboard` |
| [Visa CLI](https://visacli.sh) | Payments | Agent payment rail — pay for APIs without key management (beta) | CLI | `visa-cli init` |

## x402 APIs

Official protocol APIs accessible via [x402](https://www.x402.org/) micropayments (USDC on Base). Requires [AgentCash](https://agentcash.dev) or any x402-compatible wallet.

| Protocol | Description | Origin | Endpoints | Price |
|----------|-------------|--------|-----------|-------|
| [Nansen](https://nansen.ai) | Smart money flows, wallet profiling, token screener, PnL, prediction markets | `api.nansen.ai` | 50+ | $0.01–$7.50 |
| [Zapper](https://zapper.xyz) | Portfolio, DeFi balances, NFTs, tx history, token rankings across 60+ chains | `public.zapper.xyz` | 17 | $0.001–$0.005 |
| [StableCrypto](https://stablecrypto.dev) | CoinGecko + DefiLlama + Alchemy + Etherscan aggregated behind x402 | `stablecrypto.dev` | 90+ | $0.01 |

---

*Know of a skill, MCP server, or agent integration we're missing? [Open a PR](https://github.com/maxyz-xyz/DEGEN.md/pulls).*
