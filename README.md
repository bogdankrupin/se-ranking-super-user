# SE Ranking Super User

A shareable Claude **plugin** that bundles three SE Ranking skills into one installable unit for your whole team. Distributed as a Claude plugin marketplace (a GitHub repo with a `marketplace.json` catalog), so everyone installs the same tooling once and stays in sync.

## What's inside

This plugin (`se-ranking-super-user`) ships three skills:

| Skill | What it does |
| --- | --- |
| `se-ranking-analyst` | Pulls, analyzes, and reports on SE Ranking data — keyword rankings, backlinks, AI/LLM search visibility, SERPs, and site audits. Computes period-over-period deltas and produces weekly/monthly client reports. |
| `se-ranking-api-docs` | Documentation concierge for the SE Ranking Data API, Project API, and MCP server. Grounds every answer in the official docs with a direct citation to the exact section of `https://seranking.com/api.html`. |
| `influencer-profile-board` | Builds a rich, interactive single-file HTML profile board for any public figure or creator, enriched with live AI-search data (how they show up in ChatGPT and Google AI Overviews / AI Mode) when SE Ranking is available. |

## Requirements

- The `se-ranking-analyst` and `se-ranking-api-docs` skills work best with the **SE Ranking MCP connector** enabled, or the SE Ranking API available in a pipeline. The plugin does not bundle the connector — enable it once per user (Settings → Connectors) and authenticate.
- `influencer-profile-board` needs web search and the ability to write an HTML file; its live AI-search layer is optional and falls back to web search alone.

## Install

### Claude Code (CLI)

```bash
# 1. Add this marketplace
/plugin marketplace add bogdankrupin/se-ranking-super-user

# 2. Install the plugin
/plugin install se-ranking-super-user@se-ranking
```

Update later with `/plugin marketplace update se-ranking`.

To require it across a project automatically, add this to the project's `.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "se-ranking": {
      "source": { "source": "github", "repo": "bogdankrupin/se-ranking-super-user" }
    }
  },
  "enabledPlugins": {
    "se-ranking-super-user@se-ranking": true
  }
}
```

### Claude Cowork (desktop, org-managed)

An admin can add this repo as a marketplace in **Organization settings → Plugins** (GitHub sync), then set the plugin to *Installed by default* / *Available* / *Required* for the relevant groups. Members get it without touching a terminal.

## Auto-refresh

`.github/workflows/refresh-doc-map.yml` runs every Monday (and on demand from the Actions tab) to keep `skills/se-ranking-api-docs/references/doc-map.md` mirrored to the live SE Ranking docs sidebar. Answer content is always read live by the skill; this only refreshes the URL/anchor snapshot.

## FAQ

**Is this an official Anthropic or SE Ranking plugin?**
No. It's a community toolkit that packages SE Ranking workflows as Claude skills.

**What's the difference between a skill and a plugin?**
A skill is a single instruction set. A plugin bundles multiple skills (plus optional commands, agents, hooks, and MCP servers) so they can be versioned and distributed together through a marketplace.

**Do I need a paid SE Ranking account?**
The analyst and docs skills are most useful with SE Ranking API/MCP access. The influencer board works on web search alone, with SE Ranking as an optional enrichment.

**How do I update after the author pushes changes?**
Claude Code: `/plugin marketplace update se-ranking`. Cowork: the org marketplace re-syncs from GitHub.

## License

MIT
