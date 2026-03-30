# html-games

A collection of browser-based games built as single HTML files. Each game is self-contained with inline CSS and JavaScript — no frameworks, no build steps.

## For Claude Code (AI Agent)

This repo is configured for use with [Claude Code](https://claude.ai/code). On session start, a hook automatically sets up:

- **Chrome for Testing** (headless, with CDP)
- **Playwright MCP** (browser automation)
- **Chrome DevTools MCP** (browser inspection)

See `CLAUDE.md` for full agent instructions and `instructions/` for detailed docs.

### Running with Full Permissions

> **WARNING: This project is designed to run inside a disposable VM environment** (e.g., Claude Code on the web). It is **not safe** to run on a personal machine or any environment with sensitive data.

`.claude/settings.json` in this repo already sets `"defaultMode": "bypassPermissions"`, which means Claude Code will run **without any permission prompts** by default when you open this project. This was done intentionally so the agent can build, test, and deploy games autonomously in an isolated sandbox.

You can also launch explicitly with:

```bash
claude --dangerously-skip-permissions
```

> **DANGER: Bypass permissions disables ALL permission checks and safety prompts.** Claude will be able to execute arbitrary shell commands, modify/delete any file, install packages, and make network requests — all without asking for confirmation.
>
> **ONLY use this in isolated, disposable environments** (cloud VMs, containers, sandboxes) where:
> - There are no personal files, credentials, or secrets
> - There is no access to production systems or sensitive APIs
> - The environment can be destroyed and recreated at will
>
> **NEVER use this on your personal computer, work machine, or any environment with sensitive data.** There is no undo button. You have been warned.

## Playing the Games

Each game is a standalone `.html` file. Just open it in any modern browser:

```bash
# Clone and open a game
git clone https://github.com/rigrergl/html-games.git
open html-games/snake.html  # or any game file
```

Or use the GitHub preview links (available in PRs/branches).
