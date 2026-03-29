# HTML Games - Environment Overview

This project is a collection of browser-based games, each built as a **single HTML file** with inline CSS and JavaScript (vanilla, no frameworks).

## Architecture

```
html-games/
├── CLAUDE.md                  # Main instructions (start here)
├── .mcp.json                  # MCP server configuration (auto-loaded by Claude Code)
├── .claude/
│   ├── settings.json          # Hooks and permissions configuration
│   └── hooks/
│       └── setup-environment.sh  # Auto-installs browser + launches Chrome CDP
├── instructions/              # Detailed docs (you are here)
│   ├── 01-overview.md         # This file - project overview
│   ├── 02-mcp-servers.md      # MCP server details and usage
│   ├── 03-game-format.md      # Game file format specification
│   ├── 04-testing-workflow.md # How to test games before delivery
│   └── 05-preview-links.md   # How to generate preview links
└── *.html                     # Game files (e.g., snake.html, tetris.html)
```

## What Happens on Session Start

1. The `SessionStart` hook runs `setup-environment.sh`
2. Downloads and installs **Chrome for Testing** (v131) from Google's CDN if not present
3. Installs `@playwright/mcp` and `chrome-devtools-mcp` npm packages globally
4. Launches Chrome in **headless mode** with Chrome DevTools Protocol on port 9222
5. Starts a local **HTTP server** on port 8080 to serve game files
6. Both MCP servers (configured in `.mcp.json`) connect to Chrome via CDP

## Key Design Decisions

- **Chrome for Testing** is used instead of Playwright's bundled Chromium because the VM proxy blocks Playwright's CDN downloads but allows `storage.googleapis.com`
- **CDP connection**: Both MCP servers connect to a single shared Chrome instance via `--cdp-endpoint` / `--browserUrl` to port 9222
- **HTTP server**: Games are served via `http://localhost:8080/` rather than `file://` protocol to avoid browser security restrictions
- **Headless mode**: Uses `--headless=new` (Chrome's new headless mode) which provides full browser capabilities without a GUI
