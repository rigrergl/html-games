# Testing Workflow

Before delivering a game to the user, **always test it yourself**.

## Dedicated Scratch Space

**Never create temporary scripts, screenshots, or videos in the project root.** Use the `.scratch/` directory for all intermediate work. This directory is gitignored to keep the repository clean.

- **Temporary test scripts:** `.scratch/test-game.py`, `.scratch/check-logic.js`
- **Temporary screenshots/videos:** `.scratch/debug-1.png`, `.scratch/gameplay.webm`
- **Logs/Output:** `.scratch/output.txt`

## Step-by-Step Testing Process

### 1. Create the game file

Write the HTML file in the game's subfolder:
```
games/game-name/game-name.html
```

### 2. Create a test script in .scratch/

Do not create test files in the root. Use `.scratch/`:
```bash
# Example: Create a playwright test script
touch .scratch/test_game_v1.py
```

### 3. Open it with Playwright

Use `browser_navigate` (for MCP) or `page.goto` (for native scripts) to open the game via the local HTTP server:
```
http://localhost:8080/games/game-name/game-name.html
```

**Important:** Use `http://localhost:8080/` (or port 8000) URLs, not `file://` paths.

### 4. Capture debug artifacts in .scratch/

Save temporary screenshots, videos, or logs to `.scratch/` while you are debugging.
```python
# In your test script:
page.screenshot(path=".scratch/temp_visual_check.png")
```

### 5. Check for errors

Check for JavaScript errors in the console.

### 6. Test responsiveness

Games **MUST** be responsive. Test at multiple screen sizes:

```
Mobile portrait:  375 × 667   (iPhone SE)
Mobile landscape: 667 × 375
Tablet:           768 × 1024
Desktop:          1280 × 800
```

### 7. Take a final screenshot

Capture the game in an active state (desktop viewport) to confirm everything works.

Save it as `screenshot.png` in the game's folder — it will be used in the README:
```
games/game-name/screenshot.png
```

### 8. Clean up .scratch/

When your task is complete, delete the contents of `.scratch/` to leave the environment ready for the next task.

## Common Issues

- **Canvas not rendering** — Check that canvas dimensions are set in HTML or JS
- **Event listeners not firing** — Ensure DOM is loaded before attaching (`DOMContentLoaded`)
- **Animation not smooth** — Use `requestAnimationFrame`, not `setInterval`
- **Game doesn't start** — Some games need a user click to begin (especially with audio)
- **Blank page** — Check `browser_console_messages` for JS errors
