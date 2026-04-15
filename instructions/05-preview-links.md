# Preview Links

## Two Kinds of Preview Links

### 1. Feature branch link — put this in the PR description

Used when delivering the game during development (before the PR is merged):

```
https://htmlpreview.github.io/?https://github.com/rigrergl/html-games/blob/{BRANCH_NAME}/games/{GAME_NAME}/{GAME_NAME}.html
```

Example:
```
https://htmlpreview.github.io/?https://github.com/rigrergl/html-games/blob/feat/add-snake-game-12345/games/snake/snake.html
```

### 2. Main branch link — put this in the game's README.md

Used in the `README.md` inside the game's folder. Points to `main` as if the PR has been merged:

```
https://htmlpreview.github.io/?https://github.com/rigrergl/html-games/blob/main/games/{GAME_NAME}/{GAME_NAME}.html
```

Example:
```
https://htmlpreview.github.io/?https://github.com/rigrergl/html-games/blob/main/games/snake/snake.html
```

## Workflow

1. **Commit** the game files to the current branch
2. **Push** to the remote branch
3. **Share** the feature branch preview link in the Pull Request description
4. The README already contains the main-branch link for post-merge access

## Important Notes

- Always use the **exact branch name that you pass to the submit tool** for the feature branch link. **Do not use `git branch --show-current`**, as this provides an internal workspace branch that is not the actual remote feature branch. Keep track of the branch name you intend to submit to.
- The file must be **pushed to the remote** before the preview link will work
- `htmlpreview.github.io` renders the HTML with full CSS/JS support
- Always push before sharing the link
- The game path is always `games/{game-name}/{game-name}.html`

## Alternative: Raw GitHub Content

For simple viewing (no rendering):
```
https://raw.githubusercontent.com/rigrergl/html-games/{BRANCH_NAME}/games/{GAME_NAME}/{GAME_NAME}.html
```
