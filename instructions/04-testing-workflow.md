# Testing Workflow

Before delivering a game to the user, **always test it yourself** using the MCP servers.

## Prerequisites

Ensure Chrome and HTTP server are running (setup hook does this automatically):
```bash
# Verify Chrome CDP is running
curl -s http://localhost:9222/json/version

# Verify HTTP server is serving files
curl -s http://localhost:8080/
```

If either is down, run: `./.claude/hooks/setup-environment.sh`

## Step-by-Step Testing Process

### 1. Create the game file

Write the HTML file in the game's subfolder:
```
/home/user/html-games/games/game-name/game-name.html
```

### 2. Open it with Playwright MCP

Use `browser_navigate` to open the game via the local HTTP server:
```
http://localhost:8080/games/game-name/game-name.html
```

**Important:** Use `http://localhost:8080/` URLs, not `file://` paths.

### 3. Take a screenshot

Use `browser_take_screenshot` to visually verify:
- The game renders correctly
- Layout looks right
- No obvious visual bugs

### 4. Check the accessibility snapshot

Use `browser_snapshot` to get a text representation of the page. This shows:
- Element structure and hierarchy
- Button labels and text content
- Element refs for interaction

### 5. Test interactivity

Use `browser_click` (with refs from snapshot), `browser_press_key`, and `browser_type` to:
- Start the game
- Play a few moves/actions
- Verify game mechanics work

### 6. Check for errors

Use `browser_console_messages` to check for JavaScript errors.

Or use `browser_evaluate` to run JS in the page:
```javascript
document.querySelectorAll('canvas').length  // verify canvas exists
```

### 7. Test responsiveness on multiple viewports

Games **MUST** be responsive. Use `browser_resize` (Playwright MCP) or `mcp__chrome-devtools__emulate` to test at multiple screen sizes:

```
Mobile portrait:  375 × 667   (iPhone SE)
Mobile landscape: 667 × 375
Tablet:           768 × 1024
Desktop:          1280 × 800
```

For each viewport:
- Take a screenshot to verify layout doesn't break
- Verify on-screen touch controls appear and are tappable on mobile sizes
- Verify text/UI elements don't overflow or get clipped
- Verify the game canvas/play area scales correctly

Example using Playwright MCP:
```
browser_resize({ width: 375, height: 667 })   # mobile
browser_take_screenshot()
browser_resize({ width: 1280, height: 800 })  # desktop
browser_take_screenshot()
```

### 8. Take a final screenshot

Capture the game in an active state (desktop viewport) to confirm everything works.

Save it as `screenshot.png` in the game's folder — it will be used in the README:
```
/home/user/html-games/games/game-name/screenshot.png
```

## Common Issues

- **Canvas not rendering** — Check that canvas dimensions are set in HTML or JS
- **Event listeners not firing** — Ensure DOM is loaded before attaching (`DOMContentLoaded`)
- **Animation not smooth** — Use `requestAnimationFrame`, not `setInterval`
- **Game doesn't start** — Some games need a user click to begin (especially with audio)
- **Blank page** — Check `browser_console_messages` for JS errors
