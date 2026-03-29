# Game File Format

Every game is a **single HTML file**. No external dependencies, no build step.

## Naming Convention

```
game-name.html
```

Examples: `snake.html`, `tetris.html`, `flappy-bird.html`, `memory-match.html`

- Lowercase, hyphen-separated
- Named after the game

## File Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
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

## Rules

1. **Single file** — Everything in one `.html` file
2. **Inline styles** — All CSS in a `<style>` tag in `<head>`
3. **Inline scripts** — All JS in a `<script>` tag before `</body>`
4. **Vanilla only** — No external libraries, CDNs, or frameworks
5. **Self-contained** — Must work when opened directly in a browser (`file://` protocol)
6. **Responsive** — Should work on different screen sizes where reasonable
