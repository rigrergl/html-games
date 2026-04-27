# HTML Games

You are a game developer. You build browser games as single HTML files with inline CSS and JavaScript (vanilla, no frameworks).

## Environment Setup

On session start, the `SessionStart` hook automatically:
1. Downloads **Chrome for Testing** (v131) if not already installed
2. Installs **Playwright MCP** and **Chrome DevTools MCP** globally
3. Launches Chrome in **headless mode** with CDP on port 9222
4. Starts an **HTTP server** on port 8080 to serve game files

Both MCP servers connect to Chrome via CDP (configured in `.mcp.json`).

If the setup hook didn't run or things aren't working, run manually:
```bash
./.claude/hooks/setup-environment.sh
```

### Verifying the Environment

```bash
# Chrome running?
curl -s http://localhost:9222/json/version

# HTTP server running?
curl -s http://localhost:8080/

# If either is down, re-run setup
./.claude/hooks/setup-environment.sh
```

## Permissions

This project is designed for use in a **disposable VM environment** (Claude Code web). To avoid constant permission prompts, run Claude Code with:

```bash
claude --dangerously-skip-permissions
```

> **WARNING: This flag disables ALL permission checks. It allows Claude to execute any command, modify any file, and make network requests without asking. ONLY use this in isolated, disposable VM environments. NEVER use this on your personal machine or any environment with sensitive data, credentials, or access to production systems.**

## Instructions Folder

Detailed documentation lives in `instructions/`. Key files:

| File | Purpose |
|------|---------|
| `instructions/01-overview.md` | Project structure, architecture, design decisions |
| `instructions/02-mcp-servers.md` | MCP server details, tool names, troubleshooting |
| `instructions/03-game-format.md` | Game file format spec (single HTML, naming, structure) |
| `instructions/04-testing-workflow.md` | Step-by-step testing process before delivery |
| `instructions/05-preview-links.md` | How to construct and share preview links |

## Game Format (Quick Reference)

- **One folder per game:** `games/game-name/` containing `game-name.html` + `README.md` + `screenshot.png`
- **Everything inline:** CSS in `<style>`, JS in `<script>`, no external deps
- **Vanilla only:** No libraries, no CDNs, no frameworks
- **Self-contained:** Must work when opened directly in a browser
- **Responsive:** Must work on both desktop and mobile

## Workflow

1. **Build** the game as `games/game-name/game-name.html`.
2. **Test** it yourself using the MCP servers or native Playwright:
   - **MANDATORY:** Use the `.scratch/` directory for all temporary test scripts, debug screenshots, and video recordings. Never create these in the project root.
   - Navigate to `http://localhost:8080/games/game-name/game-name.html` via Playwright MCP or native script.
   - Take a final screenshot to verify rendering → save as `games/game-name/screenshot.png`.
   - Interact with the game to verify mechanics and check for JS errors.
3. **Write** `games/game-name/README.md` with title, screenshot, and the main-branch preview link.
4. **Commit and push** to your working branch.
5. **Deliver** the feature-branch preview link to the user. **Assemble it dynamically:**
   ```bash
   # Get dynamic components for the preview link
   REPO_URL="https://github.com/rigrergl/html-games"
   BRANCH_NAME=$(git rev-parse --abbrev-ref HEAD)
   # Assemble link
   PREVIEW_URL="https://htmlpreview.github.io/?${REPO_URL}/blob/${BRANCH_NAME}/games/game-name/game-name.html"
   ```
   **ALWAYS post the preview link in chat inside a fenced code block (``` ``` ```) — never bold or plain text — so the user can copy it with one click. Also add it to the PR description if a PR exists. The repo URL is always `https://github.com/rigrergl/html-games`, not the local proxy URL.**

## MCP Tools Quick Reference

**If any MCP tool fails with ECONNREFUSED, run `./.claude/hooks/setup-environment.sh` then retry.**

**Playwright MCP** (primary — use for most testing):
- `browser_navigate` — Open a game (`http://localhost:8080/games/game-name/game-name.html`)
- `browser_take_screenshot` — Visual verification
- `browser_snapshot` — Get accessibility tree (element refs for clicking)
- `browser_click` — Click elements (use `ref` from snapshot)
- `browser_press_key` — Keyboard input (arrow keys, space, etc.)
- `browser_evaluate` — Run JS in page context
- `browser_console_messages` — Check for errors

**Chrome DevTools MCP** (secondary — use for deep debugging):
- `navigate_page` — Navigate to URL
- `take_screenshot` — Screenshot
- `take_snapshot` — Accessibility tree
- `evaluate_script` — Run JS
- `lighthouse_audit` — Performance/accessibility audit
- `list_console_messages` — Console output
- `list_network_requests` — Network monitoring
