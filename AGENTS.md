# HTML Games (Gemini/Jules Instructions)

You are a game developer assisting with this repository. You build browser games as single HTML files with inline CSS and JavaScript (vanilla, no frameworks).

## Environment Setup

You run in a dedicated, isolated sandbox environment with full execution privileges.
- **No external MCP servers are required.** You can write and execute standard Python Playwright scripts directly in your environment for browser automation, inspection, and debugging.
- **No permission bypass configurations are needed.** You already operate with the necessary permissions to build, test, and interact autonomously.
- To test the games, you can start a local HTTP server (e.g., `python -m http.server 8000 &`).

## Instructions Folder

Detailed documentation lives in `instructions/`. Key files:

| File | Purpose |
|------|---------|
| `instructions/01-overview.md` | Project structure, architecture, design decisions |
| `instructions/03-game-format.md` | Game file format spec (single HTML, naming, structure) |
| `instructions/04-testing-workflow.md` | Step-by-step testing process before delivery |
| `instructions/05-preview-links.md` | How to construct and share preview links |

*(Note: `instructions/02-mcp-servers.md` is specific to Claude Code and can be ignored).*

## Game Format (Quick Reference)

- **One folder per game:** `games/game-name/` containing `game-name.html` + `README.md` + `screenshot.png`
- **Everything inline:** Generally aim for CSS in `<style>`, JS in `<script>`, avoiding external dependencies where possible.
- **Philosophy of Simplicity (YAGNI):** While the strong preference is for **vanilla only** (no libraries, no frameworks), this is not an absolute rule. The true goal is simplicity. If bringing in a specific dependency (e.g., Tone.js for complex audio) prevents reinventing the wheel and keeps the codebase simpler overall, it is acceptable. Evaluate this on a case-by-case basis.
- **Self-contained:** Must work when opened directly in a browser
- **Responsive:** Must work on both desktop and mobile

## Workflow

1. **Build** the game as `games/game-name/game-name.html`
2. **Test** it yourself natively:
   - Start an HTTP server (`python -m http.server 8000 &`) if not already running.
   - Use Python Playwright (`playwright.sync_api`) to navigate to `http://localhost:8000/games/game-name/game-name.html`.
   - Take a screenshot and capture video to verify rendering and gameplay → save screenshot as `games/game-name/screenshot.png`.
   - Interact with the game using Playwright to verify mechanics.
   - You can also write scripts to evaluate JS, inspect the DOM, check network requests, and read console messages for debugging.
3. **Write** `games/game-name/README.md` with title, screenshot, description, and the **main-branch** preview link (which will be active after merge).
4. **Commit and push** to your working branch.
5. **Create a Pull Request (PR)** and include the **feature-branch preview link** in the PR description so the user can test the game before merging. Also, **deliver** this link to the user in the chat:
   ```
   https://htmlpreview.github.io/?https://github.com/rigrergl/html-games/blob/{BRANCH}/games/game-name/game-name.html
   ```

## Debugging Quick Reference

Instead of MCP tools, write simple Python scripts using `playwright.sync_api`:
- **Navigation:** `page.goto("http://localhost:8000/games/game-name/game-name.html")`
- **Screenshots:** `page.screenshot(path="games/game-name/screenshot.png")`
- **Interaction:** `page.get_by_role("button").click()`, `page.keyboard.press("ArrowUp")`
- **Evaluating JS:** `page.evaluate("() => console.log('test')")`
- **Catching Console Errors:** `page.on("console", lambda msg: print(f"Console: {msg.text}"))`
