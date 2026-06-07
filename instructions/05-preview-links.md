# Preview Links

## Two Kinds of Preview Links

### 1. Feature branch link — put this in the PR description

Used when delivering the game during development (before the PR is merged):

```
https://htmlpreview.github.io/?https://github.com/rigrergl/html-games/blob/{COMMIT_SHA}/games/{GAME_NAME}/{GAME_NAME}.html
```

#### How to construct the correct link:
Because the automated system dynamically appends a unique ID to your remote branch name during submission, it is **impossible** to predict the branch name.
Instead, construct the preview link using the exact Git commit SHA of your final commit before calling the submit tool (`git rev-parse HEAD`).

```
https://htmlpreview.github.io/?https://github.com/rigrergl/html-games/blob/<EXACT_COMMIT_SHA>/games/{GAME_NAME}/{GAME_NAME}.html
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

1. **Commit** the game files to the current branch.
2. **Push** to the remote branch.
3. **Assemble** the feature branch preview link using the exact commit SHA as above.
4. **Share** the link in the Pull Request description and in the chat with the user.
5. The README already contains the main-branch link for post-merge access.

## Important Notes

- **Never omit `https://htmlpreview.github.io/?`**. This is required to render the HTML.
- Always use the **exact Git commit SHA** (`git rev-parse HEAD`) instead of the branch name. This avoids the unpredictable branch renaming issue.
- The file must be **pushed to the remote** before the preview link will work.
- The game path is always `games/{game-name}/{game-name}.html`.
