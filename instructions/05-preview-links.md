# Preview Links

## Two Kinds of Preview Links

### 1. Feature branch link — put this in the PR description

Used when delivering the game during development (before the PR is merged):

```
https://htmlpreview.github.io/?https://github.com/rigrergl/html-games/blob/{BRANCH_NAME}/games/{GAME_NAME}/{GAME_NAME}.html
```

#### How to construct the correct link:
Never guess the branch name using local bash commands (like `git rev-parse` or `gh pr view`). Your internal workspace branch is different from the actual remote branch.
Instead, manually substitute the exact `branch_name` parameter string that you plan to pass to the `submit` tool into the link.

```
https://htmlpreview.github.io/?https://github.com/rigrergl/html-games/blob/<EXACT_SUBMIT_BRANCH_NAME>/games/{GAME_NAME}/{GAME_NAME}.html
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
3. **Assemble** the feature branch preview link using the manually specified branch name as above.
4. **Share** the link in the Pull Request description and in the chat with the user.
5. The README already contains the main-branch link for post-merge access.

## Important Notes

- **Never omit `https://htmlpreview.github.io/?`**. This is required to render the HTML.
- Always use the **exact branch name** that is on the remote. **Do not guess** using local bash commands. It must match the string passed to your submit tool exactly.
- The file must be **pushed to the remote** before the preview link will work.
- The game path is always `games/{game-name}/{game-name}.html`.
