# Preview Links

After testing, deliver an **HTML preview link** to the user that points to the branch you're working on.

## GitHub Pages Raw Preview

Use this URL format to give the user a live preview via `htmlpreview.github.io`:

```
https://htmlpreview.github.io/?https://github.com/rigrergl/html-games/blob/{BRANCH_NAME}/{GAME_FILE}
```

Example:
```
https://htmlpreview.github.io/?https://github.com/rigrergl/html-games/blob/claude/add-snake-game/snake.html
```

## Alternative: Raw GitHub Content

For simple viewing (no rendering):
```
https://raw.githubusercontent.com/rigrergl/html-games/{BRANCH_NAME}/{GAME_FILE}
```

## Workflow

1. **Commit** the game file to the current branch
2. **Push** to the remote branch
3. **Construct** the preview URL using the branch name
4. **Share** the preview link with the user

## Important Notes

- Always use the **current working branch name** — check with `git branch --show-current`
- The file must be **pushed to the remote** before the preview link will work
- `htmlpreview.github.io` renders the HTML with full CSS/JS support
- Always push before sharing the link
