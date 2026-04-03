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

- 1inch (MCP, skill)
- Alchemy (MCP)
- BNB Chain (MCP)
- Chainlink (skill)
- Circle (agent kit)
- Coinbase AgentKit (MCP)
- CoinGecko (MCP, CLI)
- DefiLlama (MCP, skill)
- Dune (skill)
- Etherscan (MCP)
- GMX (skill)
- Messari (skill)
- MetaMask (MCP)
- Nansen (MCP)
- Octav (MCP, CLI)
- OpenZeppelin (MCP, skill)
- Pendle (plugin, MCP)
- QuickNode (MCP)
- Tenderly (MCP)
- Trail of Bits (plugin)
- Uniswap (plugin, skill)
- WalletConnect (skill, CLI)
- Worldcoin (skill, CLI)
- Wormhole (skill)
- Zapper (MCP, skill)

## Integrations

Official implementations only — no community or third-party wrappers.

| Protocol | Category | Description | Type | Auth | Free tier? | llms.txt | Install |
|----------|----------|-------------|------|------|------------|----------|---------|
| [1inch](https://github.com/1inch/1inch-ai) | DeFi | Token swaps, limit orders, SDK examples, and authenticated product API access across EVM chains | MCP | — | Yes | [llms.txt](https://business.1inch.com/llms.txt) | `claude mcp add --transport http 1inch https://api.1inch.com/mcp/protocol` |
| [GMX](https://github.com/gmx-io/gmx-ai) | DeFi | Trade perpetuals (up to 100x leverage) and swap tokens on GMX V2 — positions, markets, liquidity pools, GLV vaults on Arbitrum/Avalanche | Skill | — | Yes | [llms.txt](https://docs.gmx.io/llms.txt) | `npx skills add gmx-io/gmx-ai` |
| [Pendle](https://github.com/pendle-finance/pendle-ai) | DeFi | Yield trading on 7 EVM chains — swap fixed/variable yield tokens, manage LP positions, place limit orders, query APYs and market data | Plugin | — | Yes | [llms.txt](https://docs.pendle.finance/llms.txt) | `/plugin marketplace add pendle-finance/pendle-ai` |
| [Uniswap](https://github.com/Uniswap/uniswap-ai) | DeFi | Swap integration, v4 hook development, CCA auctions, liquidity planning, pay-with-any-token via x402 | Plugin | — | Yes | [llms.txt](https://docs.uniswap.org/llms.txt) | `/plugin marketplace add Uniswap/uniswap-ai` |
| [Alchemy](https://github.com/alchemyplatform/alchemy-mcp-server) | Data | Node infrastructure — token balances, prices, NFT metadata, transfer history, tx simulation, raw JSON-RPC passthrough | MCP | `ALCHEMY_API_KEY` | Yes | [llms.txt](https://www.alchemy.com/docs/llms.txt) | `claude mcp add alchemy -- npx -y @alchemy/mcp-server` |
| [CoinGecko CLI](https://github.com/coingecko/coingecko-cli) | Data | Market data — real-time prices, OHLC candles, trending coins, categories, exchange volumes, 10y+ history, live WebSocket streaming | CLI | `cg auth` | Yes (demo) | [llms.txt](https://docs.coingecko.com/llms.txt) | `brew install coingecko/coingecko-cli/cg` |
| [CoinGecko MCP](https://github.com/coingecko/coingecko-typescript/tree/main/packages/mcp-server) | Data | CoinGecko API as MCP — prices, markets, OHLC, onchain pools, DEX data, 200+ chains, 8M+ tokens | MCP | `COINGECKO_DEMO_API_KEY` | Yes (demo) | [llms.txt](https://docs.coingecko.com/llms.txt) | `claude mcp add coingecko -- npx -y @coingecko/coingecko-mcp` |
| [DefiLlama](https://github.com/DefiLlama/defillama-skills) | Data | DeFi analytics — TVL, yields, fees, revenue, stablecoins, bridges, ETF flows, token unlocks, hacks, treasury, oracle coverage across 200+ chains (23 MCP tools + 10 skills) | MCP | OAuth login | No | [llms.txt](https://api-docs.defillama.com/llms.txt) | `claude mcp add defillama --transport http https://mcp.defillama.com/mcp` |
| [Dune](https://github.com/duneanalytics/skills) | Data | Analytics — write DuneSQL queries over decoded contract tables, search datasets, manage saved queries; Sim API for real-time wallet lookups | Skill | `DUNE_API_KEY` | Yes | [llms.txt](https://docs.dune.com/llms.txt) | `npx skills add duneanalytics/skills` |
| [Etherscan](https://docs.etherscan.io/mcp-docs/introduction) | Data | Block explorer — accounts, token transfers, contract ABIs/source, event logs, gas prices, proxy RPC across 60+ EVM chains | MCP | API key (bearer) | Yes | [llms.txt](https://docs.etherscan.io/llms.txt) | `claude mcp add etherscan --transport http https://mcp.etherscan.io/mcp` |
| [Messari](https://github.com/messari/skills) | Data | Crypto market intelligence — asset profiles, metrics, research, governance, protocol data via REST API and x402 | Skill | x402 | Yes | [llms.txt](https://docs.messari.io/llms.txt) | `npx skills add messari/skills` |
| [Nansen](https://docs.nansen.ai/mcp/connecting) | Data | Smart money — whale wallet tracking, DEX trades, PnL leaderboards, token holders, perp positions, prediction markets, address labels and related wallets | MCP | `NANSEN-API-KEY` or x402 | No | [llms.txt](https://docs.nansen.ai/llms.txt) | `claude mcp add --transport http nansen https://mcp.nansen.ai/ra/mcp` |
| [Octav](https://github.com/Octav-Labs/octav-api-mcp) | Data | Portfolio analytics — aggregated holdings with DeFi positions, transaction history, NAV in multiple currencies, historical snapshots across 20+ chains | MCP | `OCTAV_API_KEY` | No | [llms.txt](https://docs.octav.fi/llms.txt) | `claude mcp add octav -- npx octav-api-mcp` |
| [Zapper](https://build.zapper.xyz/skill.md) | Data | Onchain data — portfolios, DeFi/NFT balances, tx history with human-readable interpretations, token rankings, ENS/Farcaster/Lens identity resolution across 60+ chains | MCP | `x-zapper-api-key` or x402 | Yes | [agents.txt](https://build.zapper.xyz/agents.txt) | `claude mcp add zapper -- npx mcp-remote https://mcp.zapper.xyz` |
| [Chainlink](https://github.com/smartcontractkit/chainlink-agent-skills) | Infra | Oracle & messaging — CRE workflow generation, CCIP cross-chain sends, contract scaffolding, local testing, token bridging via CCT | Skill | — | Yes | [llms.txt](https://docs.chain.link/llms.txt) | `npx skills add smartcontractkit/chainlink-agent-skills` |
| [BNB Chain](https://github.com/bnb-chain/bnbchain-mcp) | Infra | BSC, opBNB, Greenfield — blocks, contracts, tokens, NFTs, transactions, wallet ops, ERC-8004 agent identities | MCP | — | Yes | — | `claude mcp add bnbchain -- npx -y @bnb-chain/mcp@latest` |
| [Circle](https://github.com/circlefin/circle-ooak) | Infra | Object-Oriented Agent Kit — secure tool execution with approval workflows for USDC transfers and blockchain payments | Agent kit | — | Yes | [llms.txt](https://developers.circle.com/llms.txt) | `pip install circle-ooak` |
| [Coinbase AgentKit](https://github.com/coinbase/agentkit) | Infra | Agent wallet — gives your agent a Smart Contract Account to swap tokens, send transfers, stake ETH, deploy contracts, sign messages | MCP | `CDP_API_KEY_ID` + `CDP_API_KEY_SECRET` | Yes | [llms.txt](https://docs.cdp.coinbase.com/llms.txt) | `npm i @coinbase/agentkit-model-context-protocol` |
| [MetaMask](https://github.com/MetaMask/client-mcp-core) | Infra | MCP server for MetaMask Extension — lets AI agents interact with MetaMask wallet via Playwright for testing and automation | MCP | — | Yes | [llms.txt](https://docs.metamask.io/llms.txt) | `yarn add @metamask/client-mcp-core` |
| [OpenZeppelin](https://github.com/OpenZeppelin/openzeppelin-skills) | Infra | Secure smart contract development — Solidity, Cairo, Stylus, Stellar project setup, contract upgrades, code generation via MCP | Skill | — | Yes | — | `npx skills add OpenZeppelin/openzeppelin-skills` |
| [QuickNode](https://github.com/quiknode-labs/qn-mcp) | Infra | Node infrastructure management — set up endpoints, monitor usage, manage QuickNode infra through natural language | MCP | `QUICKNODE_API_KEY` | Yes | — | `claude mcp add quicknode -- npx -y @quicknode/mcp` |
| [Tenderly](https://docs.tenderly.co/mcp-server) | Infra | Dev tooling — simulate transactions before sending, trace execution, debug reverts, manage Virtual TestNets, inspect storage and state diffs | MCP | `TENDERLY_ACCESS_KEY` | Yes | [llms.txt](https://tenderly.co/llms.txt) | `claude mcp add tenderly --transport http https://mcp.tenderly.co/mcp` |
| [WalletConnect](https://github.com/WalletConnect/agent-sdk) | Infra | Wallet connection, message signing, cross-chain bridging, WCT staking from terminal — CLI + agent skills (beta) | Skill | `WALLETCONNECT_PROJECT_ID` | Yes | [llms.txt](https://docs.walletconnect.com/llms.txt) | `npx skills add WalletConnect/agent-sdk` |
| [Worldcoin](https://github.com/worldcoin/agentkit) | Infra | Agent identity — verify agents are backed by real World ID-verified humans, get free/discounted x402 access | Skill | World ID | Yes | [llms.txt](https://docs.world.org/llms.txt) | `npx skills add worldcoin/agentkit agentkit-x402` |
| [Wormhole](https://github.com/wormhole-foundation/blockchain-interop) | Infra | Cross-chain interop — product selection, NTT deployment, Connect UI integration, CCTP bridging, multi-chain governance | Skill | — | Yes | [llms.txt](https://docs.wormhole.com/llms.txt) | `npx skills add wormhole-foundation/blockchain-interop` |
| [Trail of Bits](https://github.com/trailofbits/skills) | Security | Audit tooling — smart contract vulnerability scanners, Semgrep/YARA rule authoring, variant analysis, mutation testing, property-based testing, supply chain audits | Plugin | — | Yes | [llms.txt](https://trailofbits.com/llms.txt) | `/plugin marketplace add trailofbits/skills` |

---

_Know of a skill, MCP server, or official agent integration we're missing? [Open a PR](https://github.com/maxyz-xyz/DEGEN.md/pulls)._

_Last updated: 2026-04-04_
