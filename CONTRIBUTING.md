# Contributing to DEGEN.md

Thanks for helping grow the registry. This doc explains what belongs here, how entries should be formatted, and what we've learned curating this list.

## What belongs here

DEGEN.md tracks **official agentic integrations** for Ethereum and EVM blockchains. An entry must be:

1. **Official** — published by the protocol team itself, not a community wrapper or third-party fork
2. **An agent integration** — one of: MCP server, Claude Code plugin, SKILL.md, CLI tool, or llms.txt endpoint
3. **EVM-focused** — the protocol operates on Ethereum or EVM-compatible chains. Multi-chain tooling (e.g. Thirdweb, Wormhole) is fine as long as it covers EVM. Chain-specific integrations for non-EVM chains (Solana, Aptos, etc.) are out of scope
4. **Not a library** — if it requires code-level integration (importing a package and writing setup code), it's a library, not an agent integration.

Things that do NOT belong:

- Community/third-party MCP wrappers around official APIs
- SDKs or libraries that require programmatic setup (e.g. some agent kits)
- Dev tools that happen to be CLIs but have no agent-aware features (e.g. Foundry, Hardhat)
- Non-EVM chain-specific integrations

## Entry format

### Intro list

Add a bullet in alphabetical order:

```
- Protocol Name (types comma-separated)
```

Example: `- Pendle (plugin, MCP)`

### Table row

One row per **repo**. Only split into multiple rows when the integration types live in **different repos** (e.g. CoinGecko CLI vs CoinGecko MCP, OpenZeppelin MCP vs OpenZeppelin Skills).

```
| [Protocol](https://github.com/org/repo) | Category | Description | Type | Auth | Free tier? | llms.txt | Install |
```

#### Columns

| Column          | What goes here                                                                              |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Protocol**    | Name, linked to the repo (or docs page if no public repo)                                   |
| **Category**    | `DeFi`, `Data`, `Infra`, or `Security`                                                      |
| **Description** | One line: role label + specific capabilities. Start with what it IS, then list what it does |
| **Type**        | Comma-separated: `Plugin`, `MCP`, `Skill`, `CLI`. Plugin listed first when present          |
| **Auth**        | Env var name (e.g. `ALCHEMY_API_KEY`), `x402`, `World ID`, `OAuth login`, or `—` for none   |
| **Free tier?**  | `Yes`, `Yes (demo)`, or `No`                                                                |
| **llms.txt**    | Link to the protocol's `llms.txt` (or `agents.txt`), or `—` if none exists                  |
| **Install**     | The one-liner install command. See priority below                                           |

#### Install command priority

When a protocol offers multiple integration types, the Install column should use this priority:

1. **Plugin** — `/plugin marketplace add org/repo` (bundles skills, sometimes MCP)
2. **Skill** — `npx skills add org/repo`
3. **MCP** — `claude mcp add name ...`
4. **CLI** — package manager install command

Plugins usually bundle skills and sometimes MCP servers into a single install, so prefer the plugin command unless the MCP server is in a separate repo.

#### Description style

Start with a **role label** (what kind of tool it is), then list capabilities:

- Good: `Node infrastructure — token balances, prices, NFT metadata, transfer history, tx simulation`
- Bad: `Alchemy MCP server for blockchain data`

The description should help an LLM route: "I need to do X, which tool should I install?"

## Sorting

Both the intro list and the table are sorted **alphabetically by protocol name**. When a protocol has multiple rows (different repos), group them together alphabetically by the qualified name (e.g. `CoinGecko CLI` before `CoinGecko MCP`).

## Before submitting a PR

- [ ] Entry is from the protocol's own GitHub org (official, not community)
- [ ] Protocol operates on Ethereum or EVM-compatible chains
- [ ] Type column lists ALL integration types the repo offers
- [ ] Install command follows the priority: plugin > skill > MCP > CLI
- [ ] llms.txt checked and linked if it exists
- [ ] Intro bullet list updated
- [ ] Table row is in alphabetical order
- [ ] Auth column shows the actual env var name, not just "API key"
- [ ] Free tier status is accurate
- [ ] Link goes to the repo or tool-specific docs page, not the protocol homepage
