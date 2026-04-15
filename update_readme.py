import re

with open('games/galaga/README.md', 'r') as f:
    content = f.read()

# Make sure screenshot is named correctly
content = re.sub(r'!\[.*?\]\(.*?\)', '![Galaga Gameplay](screenshot.png)', content)
# Add preview link to description if not already present
if '## Play Now' not in content:
    content += '\n\n## Play Now\n[Play Galaga](https://htmlpreview.github.io/?https://github.com/rigrergl/html-games/blob/main/games/galaga/galaga.html)'

with open('games/galaga/README.md', 'w') as f:
    f.write(content)
