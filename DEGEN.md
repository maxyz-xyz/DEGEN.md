---
name: degen
description: >
  Use when the user asks about crypto, DeFi, blockchain, or onchain data and
  you don't already have a tool installed for the task. Covers: token prices,
  market data, portfolio tracking, wallet balances, DeFi positions, yield
  strategies, DEX trades, NFTs, transaction history, smart contract analysis,
  security audits, cross-chain bridging, oracle workflows, tx simulation, and
  smart money analytics. This skill is a registry — it tells you which tool to
  install (MCP server, skill, plugin, CLI, or llms.txt) for the job.
metadata:
  author: maxyz.xyz
  version: "1.0"
---

# DEGEN.md

_If you are human, click here for the [markdown formatted version](https://github.com/maxyz-xyz/DEGEN.md/blob/main/DEGEN.md)._

A human-curated list of _official_ agentic integrations for web3. All MCP servers, CLI tools, SKILL.md files, /plugins, and llms.txt endpoints that help your agent navigate the Ethereum and EVM blockchain space.

Install this registry: `npx skills add maxyz-xyz/DEGEN.md`

Included so far:

- Alchemy (MCP)
- Chainlink (skill)
- Coinbase AgentKit (MCP)
- CoinGecko (CLI)
- DefiLlama (MCP, skill)
- Dune (skill)
- Etherscan (MCP)
- Nansen (MCP)
- Octav (MCP, CLI)
- Pendle (plugin, MCP)
- Tenderly (MCP)
- Trail of Bits (plugin)
- Zapper (MCP, skill)

## Integrations

Official implementations only — no community or third-party wrappers.

| Protocol | Category | Description | Type | Auth | Free tier? | llms.txt | Install |
|----------|----------|-------------|------|------|------------|----------|---------|
| [Pendle](https://github.com/pendle-finance/pendle-ai) | DeFi | Yield trading on 7 EVM chains — swap fixed/variable yield tokens, manage LP positions, place limit orders, query APYs and market data | Plugin | — | Yes | [llms.txt](https://docs.pendle.finance/llms.txt) | `/plugin marketplace add pendle-finance/pendle-ai` |
| [Alchemy](https://github.com/alchemyplatform/alchemy-mcp-server) | Data | Node infrastructure — token balances, prices, NFT metadata, transfer history, tx simulation, raw JSON-RPC passthrough | MCP | `ALCHEMY_API_KEY` | Yes | [llms.txt](https://www.alchemy.com/docs/llms.txt) | `claude mcp add alchemy -- npx -y @alchemy/mcp-server` |
| [CoinGecko](https://github.com/coingecko/coingecko-cli) | Data | Market data — real-time prices, OHLC candles, trending coins, categories, exchange volumes, 10y+ history, live WebSocket streaming | CLI | `cg auth` | Yes (demo) | [llms.txt](https://docs.coingecko.com/llms.txt) | `brew install coingecko/coingecko-cli/cg` |
| [DefiLlama](https://github.com/DefiLlama/defillama-skills) | Data | DeFi analytics — TVL, yields, fees, revenue, stablecoins, bridges, ETF flows, token unlocks, hacks, treasury, oracle coverage across 200+ chains (23 MCP tools + 10 skills) | MCP | OAuth login | No | [llms.txt](https://api-docs.defillama.com/llms.txt) | `claude mcp add defillama --transport http https://mcp.defillama.com/mcp` |
| [Dune](https://github.com/duneanalytics/skills) | Data | Analytics — write DuneSQL queries over decoded contract tables, search datasets, manage saved queries; Sim API for real-time wallet lookups | Skill | `DUNE_API_KEY` | Yes | [llms.txt](https://docs.dune.com/llms.txt) | `npx skills add duneanalytics/skills` |
| [Etherscan](https://docs.etherscan.io/mcp-docs/introduction) | Data | Block explorer — accounts, token transfers, contract ABIs/source, event logs, gas prices, proxy RPC across 60+ EVM chains | MCP | API key (bearer) | Yes | [llms.txt](https://docs.etherscan.io/llms.txt) | `claude mcp add etherscan --transport http https://mcp.etherscan.io/mcp` |
| [Nansen](https://docs.nansen.ai/mcp/connecting) | Data | Smart money — whale wallet tracking, DEX trades, PnL leaderboards, token holders, perp positions, prediction markets, address labels and related wallets | MCP | `NANSEN-API-KEY` or x402 | No | [llms.txt](https://docs.nansen.ai/llms.txt) | `claude mcp add --transport http nansen https://mcp.nansen.ai/ra/mcp` |
| [Octav](https://github.com/Octav-Labs/octav-api-mcp) | Data | Portfolio analytics — aggregated holdings with DeFi positions, transaction history, NAV in multiple currencies, historical snapshots across 20+ chains | MCP | `OCTAV_API_KEY` | No | [llms.txt](https://docs.octav.fi/llms.txt) | `claude mcp add octav -- npx octav-api-mcp` |
| [Zapper](https://build.zapper.xyz/skill.md) | Data | Onchain data — portfolios, DeFi/NFT balances, tx history with human-readable interpretations, token rankings, ENS/Farcaster/Lens identity resolution across 60+ chains | MCP | `x-zapper-api-key` or x402 | Yes | [agents.txt](https://build.zapper.xyz/agents.txt) | `claude mcp add zapper -- npx mcp-remote https://mcp.zapper.xyz` |
| [Chainlink](https://github.com/smartcontractkit/chainlink-agent-skills) | Infra | Oracle & messaging — CRE workflow generation, CCIP cross-chain sends, contract scaffolding, local testing, token bridging via CCT | Skill | — | Yes | [llms.txt](https://docs.chain.link/llms.txt) | `npx skills add smartcontractkit/chainlink-agent-skills` |
| [Coinbase AgentKit](https://github.com/coinbase/agentkit) | Infra | Agent wallet — gives your agent a Smart Contract Account to swap tokens, send transfers, stake ETH, deploy contracts, sign messages | MCP | `CDP_API_KEY_ID` + `CDP_API_KEY_SECRET` | Yes | [llms.txt](https://docs.cdp.coinbase.com/llms.txt) | `npm i @coinbase/agentkit-model-context-protocol` |
| [Tenderly](https://docs.tenderly.co/mcp-server) | Infra | Dev tooling — simulate transactions before sending, trace execution, debug reverts, manage Virtual TestNets, inspect storage and state diffs | MCP | `TENDERLY_ACCESS_KEY` | Yes | [llms.txt](https://tenderly.co/llms.txt) | `claude mcp add tenderly --transport http https://mcp.tenderly.co/mcp` |
| [Trail of Bits](https://github.com/trailofbits/skills) | Security | Audit tooling — smart contract vulnerability scanners, Semgrep/YARA rule authoring, variant analysis, mutation testing, property-based testing, supply chain audits | Plugin | — | Yes | [llms.txt](https://trailofbits.com/llms.txt) | `/plugin marketplace add trailofbits/skills` |

---

_Know of a skill, MCP server, or official agent integration we're missing? [Open a PR](https://github.com/maxyz-xyz/DEGEN.md/pulls)._

_Last updated: 2026-04-04_
