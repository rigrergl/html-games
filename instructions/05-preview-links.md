# Preview Links

## Two Kinds of Preview Links

### 1. Feature branch link — put this in the PR description

Used when delivering the game during development (before the PR is merged):

```
https://htmlpreview.github.io/?https://github.com/rigrergl/html-games/blob/{BRANCH_NAME}/games/{GAME_NAME}/{GAME_NAME}.html
```

#### How to derive the correct link dynamically:
Never guess the owner, repository, or branch name. Use these commands:

```bash
# 1. Get the base GitHub repository URL (e.g., https://github.com/rigrergl/html-games)
# Use 'git remote get-url origin' and strip '.git' if present
REPO_URL=$(git remote get-url origin | sed 's/\.git$//')

# 2. Get the EXACT remote branch name for the current PR
# If gh CLI is available:
BRANCH_NAME=$(gh pr view --json headRefName -jq .headRefName)
# OR if gh is not available, use the branch you just pushed to:
# BRANCH_NAME=$(git rev-parse --abbrev-ref HEAD)

# 3. Assemble the full preview link
GAME_NAME="your-game-name"
PREVIEW_URL="https://htmlpreview.github.io/?${REPO_URL}/blob/${BRANCH_NAME}/games/${GAME_NAME}/${GAME_NAME}.html"
echo $PREVIEW_URL
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
3. **Assemble** the feature branch preview link using the dynamic variables above.
4. **Share** the link in the Pull Request description and in the chat with the user.
5. The README already contains the main-branch link for post-merge access.

## Important Notes

- **Never omit `https://htmlpreview.github.io/?`**. This is required to render the HTML.
- Always use the **exact branch name** that is on the remote. **Do not guess**. Use `gh pr view` or verify the output of `git push`.
- The file must be **pushed to the remote** before the preview link will work.
- The game path is always `games/{game-name}/{game-name}.html`.
