# Game File Format

Every game lives in its own **subfolder** under `games/`. The game itself is a **single HTML file** with no external dependencies.

## Directory Structure

Each game gets its own folder:

```
games/
└── game-name/
    ├── game-name.html   ← the actual game (single HTML file)
    └── README.md        ← game description, preview link, screenshot
```

Examples:
```
games/snake/snake.html
games/tetris/tetris.html
games/conways-game-of-life/conways-game-of-life.html
```

- Folder name and HTML filename are the **same** (lowercase, hyphen-separated)
- Named after the game

## HTML File Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <title>Game Name</title>
    <style>
        /* All CSS goes here */
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { /* ... */ }
        /* Game-specific styles */
    </style>
</head>
<body>
    <!-- Game HTML structure -->

    <script>
        // All JavaScript goes here
        // Vanilla JS only - no libraries, no frameworks
    </script>
</body>
</html>
```

## HTML File Rules

1. **Single file** — Everything in one `.html` file
2. **Inline styles** — All CSS in a `<style>` tag in `<head>`
3. **Inline scripts** — All JS in a `<script>` tag before `</body>`
4. **Vanilla only** — No external libraries, CDNs, or frameworks
5. **Self-contained** — Must work when opened directly in a browser (`file://` protocol)
6. **Responsive** — Must work on both desktop and mobile screen sizes
7. **Viewport meta tag** — Always include `<meta name="viewport" ...>` for mobile

## README.md Format

Every game folder must include a `README.md` with:

1. **Game title** as an H1 heading
2. **Screenshot** — an inline image of the game in action
3. **Preview link** — pointing at the **main branch** (as if the PR has been merged)
4. **Description** — 1-3 sentences about the game

### Preview Link Format (for README — always points to main)

```
https://htmlpreview.github.io/?https://github.com/rigrergl/html-games/blob/main/games/game-name/game-name.html
```

### README Template

```markdown
# Game Name

![Screenshot](screenshot.png)

[Play Game](https://htmlpreview.github.io/?https://github.com/rigrergl/html-games/blob/main/games/game-name/game-name.html)

Brief description of the game. What it is, what makes it interesting, how to play.
```

### Screenshot

- Take a screenshot of the game in an interesting/active state using Playwright MCP
- Save it as `screenshot.png` inside the game's folder
- The screenshot should show the game running (not a blank/empty state)

## Delivery to User

When you deliver a game to the user, give them the **feature branch** preview link (not main):

```
https://htmlpreview.github.io/?https://github.com/rigrergl/html-games/blob/{BRANCH}/games/game-name/game-name.html
```

The README's link points to `main` (for after the PR is merged). The link you give the user in chat points to the current branch (so they can preview it immediately).
