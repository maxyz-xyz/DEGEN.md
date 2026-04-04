---
name: degen
description: >
  Use when the user asks about crypto, DeFi, blockchain, or onchain data and
  you don't already have a tool installed for the task. Covers: token prices,
  market data, portfolio tracking, wallet balances, DeFi positions, yield
  strategies, DEX trades, NFTs, transaction history, smart contract analysis,
  security audits, cross-chain bridging, oracle workflows, tx simulation, and
  smart money analytics. This skill is a registry — it tells you which tool 
  could be relevant (MCP server, skill, plugin, CLI, or llms.txt) for the job
  and how to install it.
metadata:
  author: maxyz.xyz
  version: "1.0"
---

# DEGEN.md

> If you are human, go here for the markdown formatted version: https://github.com/maxyz-xyz/DEGEN.md/blob/main/DEGEN.md

DEGEN.md is a human-curated list of _official_ agentic integrations for web3. All MCP servers, CLI tools, SKILL.md files, /plugins, and llms.txt endpoints that help your agent navigate Ethereum and other EVM blockchains.

Install this registry: `npx skills add maxyz-xyz/DEGEN.md`

When a protocol offers multiple integration types, prefer the **plugin**; it usually bundles skills, MCP servers, and other tools into a single install.

Included so far:

- 1inch (MCP, skill)
- Alchemy (MCP)
- BNB Chain (MCP)
- Chainlink (skill)
- CoinGecko (MCP, CLI)
- DefiLlama (MCP, skill)
- Dune (CLI, skill, MCP)
- Etherscan (MCP)
- GMX (plugin, skill)
- Messari (skill)
- MetaMask (MCP)
- Nansen (MCP)
- Octav (MCP, CLI)
- OpenZeppelin (MCP, plugin, skill)
- Pendle (plugin, MCP)
- QuickNode (MCP)
- Tenderly (MCP)
- Thirdweb (MCP)
- Trail of Bits (plugin)
- Uniswap (plugin, skill)
- WalletConnect (skill, CLI)
- World (plugin, skill, CLI)
- Wormhole (skill)
- Zapper (MCP, skill)

## Integrations

Official implementations only — no community or third-party wrappers.

| Protocol | Category | Description | Type | Auth | Free tier? | llms.txt | Install |
|----------|----------|-------------|------|------|------------|----------|---------|
| [1inch](https://github.com/1inch/1inch-ai) | DeFi | Token swaps, limit orders, SDK examples, and authenticated product API access across EVM chains | MCP | — | Yes | [llms.txt](https://business.1inch.com/llms.txt) | `claude mcp add --transport http 1inch https://api.1inch.com/mcp/protocol` |
| [Alchemy](https://github.com/alchemyplatform/alchemy-mcp-server) | Data | Node infrastructure — token balances, prices, NFT metadata, transfer history, tx simulation, raw JSON-RPC passthrough | MCP | `ALCHEMY_API_KEY` | Yes | [llms.txt](https://www.alchemy.com/docs/llms.txt) | `claude mcp add alchemy -- npx -y @alchemy/mcp-server` |
| [BNB Chain](https://github.com/bnb-chain/bnbchain-mcp) | Infra | BSC, opBNB, Greenfield — blocks, contracts, tokens, NFTs, transactions, wallet ops, ERC-8004 agent identities | MCP | — | Yes | — | `claude mcp add bnbchain -- npx -y @bnb-chain/mcp@latest` |
| [Chainlink](https://github.com/smartcontractkit/chainlink-agent-skills) | Infra | Oracle & messaging — CRE workflow generation, CCIP cross-chain sends, contract scaffolding, local testing, token bridging via CCT | Skill | — | Yes | [llms.txt](https://docs.chain.link/llms.txt) | `npx skills add smartcontractkit/chainlink-agent-skills` |
| [CoinGecko CLI](https://github.com/coingecko/coingecko-cli) | Data | Market data — real-time prices, OHLC candles, trending coins, categories, exchange volumes, 10y+ history, live WebSocket streaming | CLI | `cg auth` | Yes (demo) | [llms.txt](https://docs.coingecko.com/llms.txt) | `brew install coingecko/coingecko-cli/cg` |
| [CoinGecko MCP](https://github.com/coingecko/coingecko-typescript/tree/main/packages/mcp-server) | Data | CoinGecko API as MCP — prices, markets, OHLC, onchain pools, DEX data, 200+ chains, 8M+ tokens | MCP | `COINGECKO_DEMO_API_KEY` | Yes (demo) | [llms.txt](https://docs.coingecko.com/llms.txt) | `claude mcp add coingecko -- npx -y @coingecko/coingecko-mcp` |
| [DefiLlama MCP](https://defillama.com/mcp) | Data | DeFi analytics — TVL, yields, fees, revenue, stablecoins, bridges, ETF flows, token unlocks, hacks, treasury, oracle coverage across 200+ chains (23 tools) | MCP | OAuth login | No | [llms.txt](https://api-docs.defillama.com/llms.txt) | `claude mcp add defillama --transport http https://mcp.defillama.com/mcp` |
| [DefiLlama Skills](https://github.com/DefiLlama/defillama-skills) | Data | Guided workflows — protocol deep dives, yield strategies, risk assessment, market analysis, token research (10 skills on top of MCP) | Skill | OAuth login | No | [llms.txt](https://api-docs.defillama.com/llms.txt) | `npx skills add DefiLlama/defillama-skills` |
| [Dune CLI](https://github.com/duneanalytics/cli) | Data | Query engine — run DuneSQL from terminal, manage saved queries, monitor credit usage | CLI | `DUNE_API_KEY` | Yes | [llms.txt](https://docs.dune.com/llms.txt) | `curl -sSfL https://github.com/duneanalytics/cli/raw/main/install.sh \| bash` |
| [Dune Sim MCP](https://github.com/duneanalytics/sim-api-mcp) | Data | Real-time blockchain data — EVM/SVM transactions, balances, token info across 60+ chains via Sim API | MCP | `SIM_API_KEY` | Yes | [llms.txt](https://docs.dune.com/llms.txt) | `claude mcp add dune-sim -- npx mcp-remote http://localhost:3000/mcp` |
| [Dune Skills](https://github.com/duneanalytics/skills) | Data | Analytics — write DuneSQL queries over decoded contract tables, search datasets, manage saved queries | Skill | `DUNE_API_KEY` | Yes | [llms.txt](https://docs.dune.com/llms.txt) | `npx skills add duneanalytics/skills` |
| [Etherscan](https://docs.etherscan.io/mcp-docs/introduction) | Data | Block explorer — accounts, token transfers, contract ABIs/source, event logs, gas prices, proxy RPC across 60+ EVM chains | MCP | API key (bearer) | Yes | [llms.txt](https://docs.etherscan.io/llms.txt) | `claude mcp add etherscan --transport http https://mcp.etherscan.io/mcp` |
| [GMX](https://github.com/gmx-io/gmx-ai) | DeFi | Trade perpetuals (up to 100x leverage) and swap tokens on GMX V2 — positions, markets, liquidity pools, GLV vaults on Arbitrum/Avalanche | Plugin, Skill | — | Yes | [llms.txt](https://docs.gmx.io/llms.txt) | `/plugin marketplace add gmx-io/gmx-ai` |
| [Messari](https://github.com/messari/skills) | Data | Crypto market intelligence — asset profiles, metrics, research, governance, protocol data via REST API and x402 | Skill | x402 | Yes | [llms.txt](https://docs.messari.io/llms.txt) | `npx skills add messari/skills` |
| [MetaMask](https://github.com/MetaMask/client-mcp-core) | Infra | MCP server for MetaMask Extension — lets AI agents interact with MetaMask wallet via Playwright for testing and automation | MCP | — | Yes | [llms.txt](https://docs.metamask.io/llms.txt) | `yarn add @metamask/client-mcp-core` |
| [Nansen](https://docs.nansen.ai/mcp/connecting) | Data | Smart money — whale wallet tracking, DEX trades, PnL leaderboards, token holders, perp positions, prediction markets, address labels and related wallets | MCP | `NANSEN-API-KEY` or x402 | Yes | [llms.txt](https://docs.nansen.ai/llms.txt) | `claude mcp add --transport http nansen https://mcp.nansen.ai/ra/mcp` |
| [Octav CLI](https://github.com/Octav-Labs/octav-cli) | Data | Portfolio terminal — interactive TUI dashboard, holdings, transactions, NAV, historical snapshots, Polymarket positions across 20+ chains | CLI | `OCTAV_API_KEY` | No | [llms.txt](https://docs.octav.fi/llms.txt) | `curl -sSf https://raw.githubusercontent.com/Octav-Labs/octav-cli/main/install.sh \| sh` |
| [Octav MCP](https://github.com/Octav-Labs/octav-api-mcp) | Data | Portfolio API as MCP — aggregated holdings with DeFi positions, transaction history, NAV in multiple currencies, historical snapshots | MCP | `OCTAV_API_KEY` | No | [llms.txt](https://docs.octav.fi/llms.txt) | `claude mcp add octav -- npx octav-api-mcp` |
| [OpenZeppelin MCP](https://github.com/OpenZeppelin/openzeppelin-mcp) | Infra | Smart contract generation tools — code generation for Solidity, Cairo, Stylus, Stellar via MCP | MCP | — | Yes | — | `claude mcp add openzeppelin --transport http https://mcp.openzeppelin.com` |
| [OpenZeppelin Plugin](https://github.com/OpenZeppelin/openzeppelin-skills) | Infra | Secure smart contract development — bundles skills + MCP for project setup, contract upgrades, Solidity, Cairo, Stylus, Stellar | Plugin, Skill, MCP | — | Yes | — | `/plugin marketplace add OpenZeppelin/openzeppelin-skills` |
| [Pendle](https://github.com/pendle-finance/pendle-ai) | DeFi | Yield trading on 7 EVM chains — swap fixed/variable yield tokens, manage LP positions, place limit orders, query APYs and market data (25 MCP tools) | MCP | — | Yes | [llms.txt](https://docs.pendle.finance/llms.txt) | `/plugin marketplace add pendle-finance/pendle-ai` |
| [QuickNode](https://github.com/quiknode-labs/qn-mcp) | Infra | Node infrastructure management — set up endpoints, monitor usage, manage QuickNode infra through natural language | MCP | `QUICKNODE_API_KEY` | Yes | — | `claude mcp add quicknode -- npx -y @quicknode/mcp` |
| [Tenderly](https://docs.tenderly.co/mcp-server) | Infra | Dev tooling — simulate transactions before sending, trace execution, debug reverts, manage Virtual TestNets, inspect storage and state diffs | MCP | `TENDERLY_ACCESS_KEY` | Yes | [llms.txt](https://tenderly.co/llms.txt) | `claude mcp add tenderly --transport http https://mcp.tenderly.co/mcp` |
| [Thirdweb](https://github.com/thirdweb-dev/ai) | Infra | Full-stack web3 — chain data, wallet management, contract read/write, IPFS storage, natural language blockchain ops across 2000+ chains | MCP | `THIRDWEB_SECRET_KEY` | Yes | [llms.txt](https://portal.thirdweb.com/llms.txt) | `claude mcp add thirdweb -- uvx thirdweb-mcp` |
| [Trail of Bits](https://github.com/trailofbits/skills) | Security | Audit tooling — smart contract vulnerability scanners, Semgrep/YARA rule authoring, variant analysis, mutation testing, property-based testing, supply chain audits | Plugin, Skill | — | Yes | [llms.txt](https://trailofbits.com/llms.txt) | `/plugin marketplace add trailofbits/skills` |
| [Uniswap](https://github.com/Uniswap/uniswap-ai) | DeFi | Swap integration, v4 hook development, CCA auctions, liquidity planning, pay-with-any-token via x402 | Plugin, Skill, MCP | — | Yes | [llms.txt](https://docs.uniswap.org/llms.txt) | `/plugin marketplace add Uniswap/uniswap-ai` |
| [WalletConnect CLI](https://github.com/WalletConnect/agent-sdk/tree/main/packages/cli-sdk) | Infra | Wallet connection, message signing, cross-chain bridging, WCT staking from terminal (beta) | CLI | `WALLETCONNECT_PROJECT_ID` | Yes | [llms.txt](https://docs.walletconnect.com/llms.txt) | `npm i -g @walletconnect/cli-sdk` |
| [WalletConnect Skills](https://github.com/WalletConnect/agent-sdk/tree/main/skills) | Infra | Agent skills for wallet connection, signing, and cross-chain operations (beta) | Skill | `WALLETCONNECT_PROJECT_ID` | Yes | [llms.txt](https://docs.walletconnect.com/llms.txt) | `npx skills add WalletConnect/agent-sdk` |
| [World CLI](https://github.com/worldcoin/agentkit/tree/main/cli) | Infra | Register agent wallets with World ID — prove your agent is human-backed via AgentBook smart contract on Base | CLI | World ID | Yes | [llms.txt](https://docs.world.org/llms.txt) | `npx @worldcoin/agentkit-cli register <address>` |
| [World Plugin](https://github.com/worldcoin/agentkit) | Infra | Agent identity — World ID verification, x402 auth flow, bundles skills for free/discounted API access | Plugin, Skill | World ID | Yes | [llms.txt](https://docs.world.org/llms.txt) | `/plugin marketplace add worldcoin/agentkit` |
| [Wormhole](https://github.com/wormhole-foundation/blockchain-interop) | Infra | Cross-chain interop — product selection, NTT deployment, Connect UI integration, CCTP bridging, multi-chain governance | Skill | — | Yes | [llms.txt](https://docs.wormhole.com/llms.txt) | `npx skills add wormhole-foundation/blockchain-interop` |
| [Zapper](https://build.zapper.xyz/skill.md) | Data | Onchain data — portfolios, DeFi/NFT balances, tx history with human-readable interpretations, token rankings, ENS/Farcaster/Lens identity resolution across 60+ chains | MCP | `x-zapper-api-key` or x402 | Yes | [agents.txt](https://build.zapper.xyz/agents.txt) | `claude mcp add zapper -- npx mcp-remote https://mcp.zapper.xyz` |

---

_Know of a skill, MCP server, or official agent integration we're missing? [Open a PR](https://github.com/maxyz-xyz/DEGEN.md/pulls)._

_Last updated: 2026-04-04_
