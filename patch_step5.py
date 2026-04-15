import re

with open('games/galaga/galaga.html', 'r') as f:
    content = f.read()

# Replace Player bullets code block
player_bullets_regex = r"        // Player bullets\n        for \(let b of bullets\) \{.*?\}\n        \}"
new_player_bullets = """        // Player bullets
        for (let b of bullets) {
            ctx.imageSmoothingEnabled = false;
            if (b.supernova) {
                let hue = (frameCount * 10 + b.x * 0.5) % 360;
                ctx.fillStyle = `hsl(${hue},100%,60%)`;
                ctx.fillRect(b.x - 5 * scale, b.y - 5 * scale, 10 * scale, 10 * scale);
                ctx.fillStyle = '#fff';
                ctx.fillRect(b.x - 2 * scale, b.y - 2 * scale, 4 * scale, 4 * scale);
            } else if (b.freeze) {
                ctx.fillStyle = '#8ff';
                ctx.fillRect(b.x - 2 * scale, b.y - 8 * scale, 4 * scale, 16 * scale);
                ctx.fillStyle = '#fff';
                ctx.fillRect(b.x - 1 * scale, b.y - 6 * scale, 2 * scale, 12 * scale);
            } else if (b.ricochet) {
                ctx.fillStyle = '#ef0';
                ctx.fillRect(b.x - 4 * scale, b.y - 4 * scale, 8 * scale, 8 * scale);
                ctx.fillStyle = '#fff';
                ctx.fillRect(b.x - 2 * scale, b.y - 2 * scale, 4 * scale, 4 * scale);
            } else if (b.drone) {
                ctx.fillStyle = '#bf0';
                ctx.fillRect(b.x - 3 * scale, b.y - 3 * scale, 6 * scale, 6 * scale);
            } else if (b.drunk) {
                ctx.fillStyle = '#5f5';
                ctx.fillRect(b.x - 4 * scale, b.y - 4 * scale, 8 * scale, 8 * scale);
                ctx.fillStyle = '#fff';
                ctx.fillRect(b.x - 1.5 * scale, b.y - 1.5 * scale, 3 * scale, 3 * scale);
            } else if (b.pierce) {
                ctx.fillStyle = '#ff4';
                ctx.fillRect(b.x - 3 * scale, b.y - 10 * scale, 6 * scale, 20 * scale);
                ctx.fillStyle = '#fff';
                ctx.fillRect(b.x - 1.5 * scale, b.y - 8 * scale, 3 * scale, 16 * scale);
            } else {
                ctx.fillStyle = '#ff0';
                ctx.fillRect(b.x - 2 * scale, b.y - 7 * scale, 4 * scale, 14 * scale);
                ctx.fillStyle = '#fff';
                ctx.fillRect(b.x - 1 * scale, b.y - 5 * scale, 2 * scale, 10 * scale);
            }
        }"""
content = re.sub(player_bullets_regex, new_player_bullets, content, flags=re.DOTALL)

# Replace Enemy bullets code block
enemy_bullets_regex = r"        // Enemy bullets\n        for \(let b of enemyBullets\) \{.*?\}\n        \}"
new_enemy_bullets = """        // Enemy bullets
        for (let b of enemyBullets) {
            ctx.imageSmoothingEnabled = false;
            if (b.homing) {
                ctx.save();
                ctx.translate(b.x, b.y);
                let ang = Math.atan2(b.vy, b.vx) + Math.PI / 2;
                ctx.rotate(ang);
                ctx.fillStyle = '#f40';
                ctx.beginPath();
                ctx.moveTo(0, -7 * scale);
                ctx.lineTo(-4 * scale, 5 * scale);
                ctx.lineTo(4 * scale, 5 * scale);
                ctx.closePath();
                ctx.fill();
                ctx.fillStyle = '#ff0';
                ctx.fillRect(-1.5 * scale, -5.5 * scale, 3 * scale, 3 * scale);
                ctx.restore();
            } else if (b.cluster) {
                ctx.fillStyle = '#f80';
                ctx.save();
                ctx.translate(b.x, b.y);
                ctx.rotate(frameCount * 0.1);
                ctx.fillRect(-3 * scale, -3 * scale, 6 * scale, 6 * scale);
                ctx.restore();
            } else {
                ctx.fillStyle = '#f44';
                ctx.fillRect(b.x - 3.5 * scale, b.y - 3.5 * scale, 7 * scale, 7 * scale);
                ctx.fillStyle = '#faa';
                ctx.fillRect(b.x - 1.5 * scale, b.y - 1.5 * scale, 3 * scale, 3 * scale);
            }
        }"""
content = re.sub(enemy_bullets_regex, new_enemy_bullets, content, flags=re.DOTALL)

with open('games/galaga/galaga.html', 'w') as f:
    f.write(content)

print("Patch 5 applied.")
