# MCP Servers

Two MCP servers provide browser capabilities for testing games. Both connect to a shared headless Chrome instance running with CDP on port 9222.

## Architecture

```
┌─────────────────┐     ┌──────────────────────┐
│  Playwright MCP  │────►│                      │     ┌──────────────┐
│  (automation)    │ CDP │  Chrome Headless      │────►│ HTTP :8080   │
└─────────────────┘     │  (port 9222)          │     │ Game files   │
                        │                      │     └──────────────┘
┌─────────────────┐     │                      │
│  Chrome DevTools │────►│                      │
│  MCP (inspect)   │ CDP │                      │
└─────────────────┘     └──────────────────────┘
```

## 1. Playwright MCP (`@playwright/mcp`)

**Purpose:** Browser automation — navigate, click, type, take screenshots, read page content.

**Connection:** `--cdp-endpoint http://127.0.0.1:9222`

**Key tools:**
- `browser_navigate` — Open a URL
- `browser_take_screenshot` — Take a screenshot (requires `--caps vision`)
- `browser_snapshot` — Get accessibility tree snapshot of the page
- `browser_click` — Click on elements (use `ref` from snapshot)
- `browser_type` — Type text into inputs
- `browser_press_key` — Press keyboard keys
- `browser_evaluate` — Run JavaScript in the page context
- `browser_console_messages` — Read console output
- `browser_tabs` — List open tabs

**Typical usage:**
1. Navigate: `browser_navigate` to `http://localhost:8080/game-name.html`
2. Verify: `browser_take_screenshot` to visually check rendering
3. Interact: `browser_click`, `browser_press_key` to play the game
4. Debug: `browser_console_messages` to check for errors

## 2. Chrome DevTools MCP (`chrome-devtools-mcp`)

**Purpose:** Deep browser inspection — performance profiling, network monitoring, CSS inspection, console access.

**Connection:** `--browserUrl http://127.0.0.1:9222`

**Key tools:**
- `navigate_page` — Navigate to a URL
- `take_screenshot` — Take a screenshot
- `take_snapshot` — Get accessibility tree
- `evaluate_script` — Run JavaScript
- `list_console_messages` / `get_console_message` — Console access
- `list_network_requests` / `get_network_request` — Network monitoring
- `lighthouse_audit` — Run Lighthouse audit (accessibility, SEO, best practices)
- `performance_start_trace` / `performance_stop_trace` — Performance profiling
- `click`, `fill`, `press_key` — Interaction

**When to use which:**
| Task | Use |
|------|-----|
| Navigate + screenshot + basic interaction | Playwright MCP |
| Quick visual verification | Playwright MCP |
| Performance profiling | Chrome DevTools MCP |
| Network request debugging | Chrome DevTools MCP |
| Lighthouse audit | Chrome DevTools MCP |
| Console error investigation | Either (both have console access) |

## Troubleshooting

**MCP servers can't connect:**
```bash
# Check if Chrome is running
curl -s http://localhost:9222/json/version

# If not, restart it
pkill -f "chrome.*remote-debugging-port=9222"
/opt/chrome-for-testing/chrome-linux64/chrome --headless=new --no-sandbox --disable-gpu --remote-debugging-port=9222 &
```

**HTTP server not running:**
```bash
# Check
curl -s http://localhost:8080/ > /dev/null && echo "OK" || echo "DOWN"

# Restart
cd /home/user/html-games && python3 -m http.server 8080 &
```

## Known Issues & Learnings

### Chrome CDP disconnects between tool calls

**Symptom:** A Playwright MCP call (e.g. `browser_navigate`) succeeds, but the very next call (e.g. `browser_take_screenshot`) fails with:
```
Error: browserType.connectOverCDP: connect ECONNREFUSED 127.0.0.1:9222
```

**Root cause:** Chrome for Testing exits unexpectedly after handling one CDP request. This happens intermittently in the VM environment — the process is not supervised and can die quietly.

**Fix:** Re-run the setup script. It is idempotent and safe to run at any time:
```bash
./.claude/hooks/setup-environment.sh
```
Then retry the failing tool call. You may need to do this once or twice per session.

**Pattern to follow:** If any Playwright or Chrome DevTools MCP call fails with a connection error:
1. Run `setup-environment.sh`
2. Immediately retry the same tool call (don't skip it)
3. If it fails again, run setup once more and retry

### `browser_navigate` succeeds but `browser_take_screenshot` fails

This is the same root cause above — Chrome dies between calls. Navigate re-launches Chrome implicitly in some configurations, but screenshot does not. Always re-run setup if screenshot errors with ECONNREFUSED.

### Favicon 404 in console

```
[ERROR] Failed to load resource: the server responded with 404 @ http://localhost:8080/favicon.ico
```

This is harmless — the HTTP server has no favicon. It does not affect game functionality. Ignore it when checking console messages.
