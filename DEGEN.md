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

- 1inch (plugin, skill, MCP)
- Alchemy (MCP)
- Base (skill, MCP)
- BNB Chain (MCP)
- Chainlink (skill)
- CoinGecko (MCP, CLI)
- DefiLlama (MCP, skill)
- DRPC (plugin, skill, MCP)
- Dune (CLI, skill, MCP)
- Etherscan (MCP, CLI, Skill)
- Fireblocks (MCP)
- GMX (plugin, skill)
- Messari (skill)
- MetaMask (MCP, skill, CLI)
- Morpho (plugin, skill, MCP)
- Nansen (MCP)
- Octav (MCP, CLI)
- OpenZeppelin (MCP, plugin, skill)
- Pendle (plugin, skill, MCP)
- Polygon (skill, CLI)
- QuickNode (MCP)
- Stake DAO (skill)
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
| [1inch](https://github.com/1inch/1inch-ai) | DeFi | Token swaps, limit orders, SDK examples, and authenticated product API access across EVM chains | Plugin, Skill, MCP | API key or OAuth for protected tools | Yes (public tools) | [llms.txt](https://business.1inch.com/llms.txt) | `claude mcp add --transport http --scope user 1inch-mcp https://api.1inch.com/mcp/protocol` |
| [Alchemy](https://www.alchemy.com/docs/alchemy-mcp-server) | Data | Node infrastructure — 168 tools spanning RPC calls, ENS resolution, token prices, NFT metadata, tx simulation/tracing, account abstraction, smart wallets, and Solana DAS across 100+ networks | MCP | OAuth (sign in with Alchemy account) | Yes | [llms.txt](https://www.alchemy.com/docs/llms.txt) | `claude mcp add alchemy --transport http https://mcp.alchemy.com/mcp` |
| [Base](https://github.com/base/skills) | Infra | Agent wallet via Base Account — balances, sends, swaps, signing, x402 payments, batched calls (EIP-5792), tx history, plus 20+ third-party DeFi/NFT plugins (Uniswap, Morpho, Aerodrome, OpenSea, etc.) | Skill, MCP | OAuth (Base Account approval) | Yes | [llms.txt](https://docs.base.org/llms.txt) | `claude mcp add --transport http base-mcp https://mcp.base.org` |
| [BNB Chain](https://github.com/bnb-chain/bnbchain-mcp) | Infra | BSC, opBNB, Greenfield — blocks, contracts, tokens, NFTs, transactions, wallet ops, ERC-8004 agent identities | MCP | `PRIVATE_KEY` optional for write/wallet ops | Yes | — | `claude mcp add bnbchain -- npx -y @bnb-chain/mcp@latest` |
| [Chainlink](https://github.com/smartcontractkit/chainlink-agent-skills) | Infra | Oracle & messaging skills — CRE workflows, CCIP transfers/CCT, Data Feeds, Data Streams, VRF, ACE compliance, confidential AI attestation | Skill | — | Yes | [llms.txt](https://docs.chain.link/llms.txt) | `npx skills add smartcontractkit/chainlink-agent-skills` |
| [CoinGecko CLI](https://github.com/coingecko/coingecko-cli) | Data | Market data — real-time prices, OHLC candles, trending coins, categories, exchange volumes, 10y+ history, paid live WebSocket streaming | CLI | `cg auth` | Yes (demo; some commands paid) | [llms.txt](https://docs.coingecko.com/llms.txt) | `brew install coingecko/coingecko-cli/cg` |
| [CoinGecko MCP](https://github.com/coingecko/coingecko-typescript/tree/main/packages/mcp-server) | Data | CoinGecko API as MCP — prices, markets, OHLC, onchain pools, DEX data, 200+ chains, 8M+ tokens | MCP | `COINGECKO_DEMO_API_KEY` or `COINGECKO_PRO_API_KEY` | Yes (demo; some endpoints paid) | [llms.txt](https://docs.coingecko.com/llms.txt) | `claude mcp add coingecko -- npx -y @coingecko/coingecko-mcp` |
| [DefiLlama MCP](https://api-docs.defillama.com) | Data | DeFi analytics — TVL, yields, fees, revenue, stablecoins, bridges, ETF flows, token unlocks, hacks, treasury, oracle coverage across 200+ chains (23 tools) | MCP | OAuth login | No | [llms.txt](https://api-docs.defillama.com/llms.txt) | `claude mcp add defillama --transport http https://mcp.defillama.com/mcp` |
| [DefiLlama Skills](https://github.com/DefiLlama/defillama-skills) | Data | Guided workflows — protocol deep dives, yield strategies, risk assessment, market analysis, token research (10 skills on top of MCP) | Skill | OAuth login | No | [llms.txt](https://api-docs.defillama.com/llms.txt) | `npx skills add DefiLlama/defillama-skills` |
| [DRPC](https://github.com/drpcorg/drpc-agent-skills) | Infra | Decentralized RPC gateway — 16 MCP tools (balances, blocks, tx receipts, logs, contract calls, gas, raw/batch JSON-RPC) across 200+ consensus-validated networks | Plugin, Skill, MCP | API key (auto via x402) or free key at drpc.org | Yes | [llms.txt](https://drpc.org/llms.txt) | `claude plugins marketplace add drpcorg/drpc-agent-skills` |
| [Dune CLI](https://github.com/duneanalytics/cli) | Data | Query engine — run DuneSQL from terminal, manage saved queries, monitor credit usage | CLI | `DUNE_API_KEY` | Yes | [llms.txt](https://docs.dune.com/llms.txt) | `curl -sSfL https://github.com/duneanalytics/cli/raw/main/install.sh \| bash` |
| [Dune MCP](https://docs.dune.com/api-reference/agents/mcp) | Data | Onchain analytics MCP — discover tables, create and run DuneSQL queries, inspect results, manage visualizations, dashboards, and usage | MCP | OAuth or `x-dune-api-key` | Yes | [llms.txt](https://docs.dune.com/llms.txt) | `claude mcp add --scope user --transport http dune https://api.dune.com/mcp/v1` |
| [Dune Skills](https://github.com/duneanalytics/skills) | Data | Analytics skills — DuneSQL queries, dataset search, saved-query management, and Sim wallet/token lookups | Skill | `DUNE_API_KEY`; `DUNE_SIM_API_KEY` for Sim | Yes | [llms.txt](https://docs.dune.com/llms.txt) | `npx skills add duneanalytics/skills` |
| [Etherscan CLI](https://github.com/etherscan/etherscan-cli) | Data | Terminal client — accounts, contracts, tokens, logs, gas, stats, and proxy RPC across 60+ EVM chains, with JSON/table/CSV output and an interactive TUI explorer | CLI | `ETHERSCAN_API_KEY` or `etherscan login` | Yes | [llms.txt](https://docs.etherscan.io/llms.txt) | `brew install etherscan/etherscan-cli/etherscan` |
| [Etherscan MCP](https://docs.etherscan.io/build-with-ai/mcp) | Data | Block explorer — accounts, token transfers, contract ABIs/source, event logs, gas prices, proxy RPC across 60+ EVM chains | MCP | `ETHERSCAN_API_KEY` bearer | Yes | [llms.txt](https://docs.etherscan.io/llms.txt) | `claude mcp add etherscan --transport http https://mcp.etherscan.io/mcp --header "Authorization: Bearer <ETHERSCAN_API_KEY>"` |
| [Etherscan Skills](https://github.com/etherscan/skills) | Data | Installable skills on top of the MCP/CLI — task orchestrator, Flow (trace/verify/visualize money flows into a case file), contract review, and transaction debugger | Skill | `ETHERSCAN_API_KEY` (resolved via CLI/MCP/env) | Yes | [llms.txt](https://docs.etherscan.io/llms.txt) | `npx skills add etherscan/skills` |
| [Fireblocks](https://github.com/fireblocks/fireblocks-mcp) | Infra | Institutional custody MCP — query/create transactions, vault accounts & balances, exchange accounts, network connections, policies, wallets, and users (write ops off by default) | MCP | `FIREBLOCKS_API_KEY` + `FIREBLOCKS_PRIVATE_KEY_PATH` | No | [llms.txt](https://developers.fireblocks.com/llms.txt) | `claude mcp add fireblocks -- npx -y @fireblocks/mcp-server` |
| [GMX](https://github.com/gmx-io/gmx-ai) | DeFi | Trade perpetuals (up to 100x leverage) and swap tokens on GMX V2 — positions, markets, liquidity pools, GLV vaults on Arbitrum/Avalanche/Botanix | Plugin, Skill | — | Yes | [llms.txt](https://docs.gmx.io/llms.txt) | `/plugin marketplace add gmx-io/gmx-ai` |
| [Messari](https://github.com/messari/skills) | Data | Crypto market intelligence — asset profiles, metrics, research, governance, protocol data via REST API and x402 | Skill | `MESSARI_API_KEY` or x402 | Yes | [llms.txt](https://docs.messari.io/llms.txt) | `npx skills add messari/skills` |
| [MetaMask](https://github.com/MetaMask/client-mcp-core) | Infra | MetaMask Extension automation — local agent daemon, `mm` CLI, and agent skill for Playwright-based wallet testing and workflows | MCP, Skill, CLI | — | Yes | [llms.txt](https://docs.metamask.io/llms.txt) | `npm install -g @metamask/client-mcp-core` |
| [Morpho](https://github.com/morpho-org/morpho-skills) | DeFi | Agent toolkit — query vaults, markets, and user positions, simulate outcomes, prepare unsigned lending transactions, and scaffold Morpho integrations on Ethereum and Base | Plugin, Skill, MCP | — | Yes | [llms.txt](https://docs.morpho.org/llms.txt) | `/plugin marketplace add morpho-org/morpho-skills` |
| [Nansen](https://docs.nansen.ai/mcp/connecting) | Data | Smart money — whale wallet tracking, DEX trades, PnL leaderboards, token holders, perp positions, prediction markets, address labels and related wallets | MCP | `NANSEN-API-KEY` | Yes | [llms.txt](https://docs.nansen.ai/llms.txt) | `claude mcp add --transport http nansen https://mcp.nansen.ai/ra/mcp --header "NANSEN-API-KEY: <NANSEN_API_KEY>"` |
| [Octav CLI](https://github.com/Octav-Labs/octav-cli) | Data | Portfolio terminal — interactive TUI dashboard, holdings, transactions, NAV, historical snapshots, Polymarket positions across 20+ chains | CLI | `OCTAV_API_KEY` or x402 for agent commands | No | [llms.txt](https://docs.octav.fi/llms.txt) | `curl -sSf https://raw.githubusercontent.com/Octav-Labs/octav-cli/main/install.sh \| sh` |
| [Octav MCP](https://github.com/Octav-Labs/octav-api-mcp) | Data | Portfolio API as MCP — aggregated holdings with DeFi positions, transaction history, NAV in multiple currencies, historical snapshots | MCP | `OCTAV_API_KEY` | No | [llms.txt](https://docs.octav.fi/llms.txt) | `claude mcp add octav -- npx -y octav-api-mcp` |
| [OpenZeppelin MCP](https://github.com/OpenZeppelin/openzeppelin-mcp) | Infra | Smart contract generation tools — code generation for Solidity, Cairo, Stylus, Stellar, Confidential Contracts, and Uniswap Hooks via MCP | MCP | — | Yes | — | `claude mcp add openzeppelin --transport http https://mcp.openzeppelin.com` |
| [OpenZeppelin Plugin](https://github.com/OpenZeppelin/openzeppelin-skills) | Infra | Secure smart contract development skills for project setup, contract upgrades, Solidity, Cairo, Stylus, Stellar | Plugin, Skill | — | Yes | — | `/plugin marketplace add OpenZeppelin/openzeppelin-skills` |
| [Pendle](https://github.com/pendle-finance/pendle-ai) | DeFi | Yield and rates trading via Pendle V2 + Boros — swap/manage LP/limit orders, query market data, and trade Arbitrum funding-rate derivatives | Plugin, Skill, MCP | — | Yes | [llms.txt](https://docs.pendle.finance/llms.txt) | `/plugin marketplace add pendle-finance/pendle-ai` |
| [Polygon Agent CLI](https://github.com/0xPolygon/polygon-agent-cli) | Infra | Agent payments toolkit — session smart contract wallets, token sends/swaps/bridges, ERC-8004 identity/reputation, x402 micropayments on Polygon | Skill, CLI | `SEQUENCE_PROJECT_ACCESS_KEY` | Yes | [llms.txt](https://docs.polygon.technology/llms.txt) | `npx skills add https://github.com/0xPolygon/polygon-agent-cli` |
| [QuickNode](https://github.com/quiknode-labs/qn-mcp) | Infra | Node infrastructure management — set up endpoints, monitor usage, manage QuickNode infra through natural language | MCP | `QUICKNODE_API_KEY` | Yes | — | `claude mcp add quicknode -- npx -y @quicknode/mcp` |
| [Stake DAO](https://github.com/stake-dao/stakedao-skills) | DeFi | Yield platform assistant — query live vaults, liquid lockers (sdCRV/sdBAL/sdFXN), token prices, merkle claims, and lending positions/health factors via the Hub API, plus protocol TVL/fees and docs navigation | Skill | — | Yes | [llms.txt](https://docs.stakedao.org/llms.txt) | `npx skills add stake-dao/stakedao-skills` |
| [Tenderly](https://docs.tenderly.co/mcp-server) | Infra | Dev tooling — simulate transactions before sending, trace execution, debug reverts, manage Virtual TestNets, inspect storage and state diffs | MCP | OAuth login (browser) | Yes | [llms.txt](https://tenderly.co/llms.txt) | `claude mcp add tenderly --transport http https://mcp.tenderly.co/mcp` |
| [Thirdweb](https://github.com/thirdweb-dev/ai) | Infra | Full-stack web3 — chain data, wallet management, contract read/write, IPFS storage, natural language blockchain ops across 2000+ chains | MCP | `THIRDWEB_SECRET_KEY` | Yes | [llms.txt](https://portal.thirdweb.com/llms.txt) | `claude mcp add thirdweb -- uvx thirdweb-mcp` |
| [Trail of Bits](https://github.com/trailofbits/skills) | Security | Audit tooling — smart contract vulnerability scanners, Semgrep/YARA rule authoring, variant analysis, mutation testing, property-based testing, supply chain audits | Plugin, Skill | — | Yes | [llms.txt](https://trailofbits.com/llms.txt) | `/plugin marketplace add trailofbits/skills` |
| [Uniswap](https://github.com/Uniswap/uniswap-ai) | DeFi | Swap integration, v4 hook development, CCA auctions, liquidity planning, pay-with-any-token via x402, automated trading (DCA, index, copy-trade) | Plugin, Skill, MCP | — | Yes | [llms.txt](https://docs.uniswap.org/llms.txt) | `/plugin marketplace add Uniswap/uniswap-ai` |
| [WalletConnect CLI](https://github.com/WalletConnect/agent-sdk/tree/main/packages/cli-sdk) | Infra | Wallet connection, message signing, cross-chain bridging, WCT staking from terminal (beta) | CLI | `WALLETCONNECT_PROJECT_ID` | Yes | [llms.txt](https://docs.walletconnect.com/llms.txt) | `npm install -g @walletconnect/cli-sdk @walletconnect/staking-cli` |
| [WalletConnect Skills](https://github.com/WalletConnect/agent-sdk/tree/main/skills) | Infra | Agent skills for wallet connection, signing, and cross-chain operations (beta) | Skill | `WALLETCONNECT_PROJECT_ID` | Yes | [llms.txt](https://docs.walletconnect.com/llms.txt) | `npx skills add WalletConnect/agent-sdk` |
| [World CLI](https://github.com/worldcoin/agentkit/tree/main/cli) | Infra | Register agent wallets with World ID — prove your agent is human-backed via AgentBook smart contract on Base | CLI | World ID | Yes | [llms.txt](https://docs.world.org/llms.txt) | `npx @worldcoin/agentkit-cli register <address>` |
| [World Plugin](https://github.com/worldcoin/agentkit) | Infra | Agent identity — World ID verification, x402 auth flow, bundles skills for free/discounted API access | Plugin, Skill | World ID | Yes | [llms.txt](https://docs.world.org/llms.txt) | `npx skills add worldcoin/agentkit agentkit-x402` |
| [Wormhole](https://github.com/wormhole-foundation/blockchain-interop) | Infra | Cross-chain interop — product selection, NTT deployment, Connect UI integration, CCTP bridging, multi-chain governance | Skill | — | Yes | [llms.txt](https://docs.wormhole.com/llms.txt) | `npx skills add wormhole-foundation/blockchain-interop` |
| [Zapper](https://build.zapper.xyz/skill.md) | Data | Onchain data — portfolios, DeFi/NFT balances, tx history with human-readable interpretations, token rankings, ENS/Farcaster/Lens identity resolution across 60+ chains | MCP, Skill | `x-zapper-api-key` or x402 | Yes | [agents.txt](https://build.zapper.xyz/agents.txt) | `claude mcp add zapper -- npx mcp-remote https://mcp.zapper.xyz` |

---

_Know of a skill, MCP server, or official agent integration we're missing? [Open a PR](https://github.com/maxyz-xyz/DEGEN.md/pulls)._

_Last updated: 2026-08-24_
