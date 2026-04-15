import re

with open('games/galaga/galaga.html', 'r') as f:
    content = f.read()

# Replace drawShip
draw_ship_regex = r"    function drawShip\(x, y, w, h\) \{.*?(?=    // Enemy types)"
new_draw_ship = """    function drawShip(x, y, w, h) {
        ctx.save();
        ctx.translate(x, y);

        // Turn off smoothing for pixel art
        ctx.imageSmoothingEnabled = false;

        // Draw player sprite
        let sprite = renderedSprites.ship;
        if (sprite) {
            ctx.drawImage(sprite.canvas, -w/2, -h/2, w, h);
        }

        // Draw animated flames
        let isMoving = keys && (keys['ArrowLeft'] || keys['a'] || keys['ArrowRight'] || keys['d']);
        let flameKey = (frameCount % 6 < 3) ? 'shipFlame1' : 'shipFlame2';
        let flameSprite = renderedSprites[flameKey];
        if (flameSprite) {
            // Adjust flame size depending on if moving
            let fHeight = isMoving ? h * 0.4 : h * 0.3;
            ctx.drawImage(flameSprite.canvas, -w/2, h/2 - 2, w, fHeight);
        }

        // Shield effect
        if (currentPowerUp === 'shield' && shieldHP > 0) {
            ctx.strokeStyle = `rgba(0,255,0,${0.3 + Math.sin(frameCount * 0.15) * 0.2})`;
            ctx.lineWidth = 2 * scale;
            ctx.beginPath();
            ctx.arc(0, 0, w * 0.85, 0, Math.PI * 2);
            ctx.stroke();
            // second ring
            ctx.strokeStyle = `rgba(0,255,0,${0.15 + Math.sin(frameCount * 0.1 + 1) * 0.1})`;
            ctx.beginPath();
            ctx.arc(0, 0, w * 0.95, 0, Math.PI * 2);
            ctx.stroke();
        }

        ctx.restore();
    }
"""
content = re.sub(draw_ship_regex, new_draw_ship, content, flags=re.DOTALL)

# Replace ENEMY_TYPES
enemy_types_regex = r"    const ENEMY_TYPES = \[.*?(?=    function spawnWave\(\) \{)"
new_enemy_types = """    const ENEMY_TYPES = [
        { // Bug
            color: '#f44',
            draw(x, y, w, h, t) {
                ctx.save(); ctx.translate(x, y);
                ctx.imageSmoothingEnabled = false;
                ctx.shadowColor = this.color;
                ctx.shadowBlur = 6 * scale;
                let spriteName = (Math.floor(t / 15) % 2 === 0) ? 'bug1' : 'bug2';
                let sprite = renderedSprites[spriteName];
                if (sprite) ctx.drawImage(sprite.canvas, -w/2, -h/2, w, h);
                ctx.shadowBlur = 0;
                ctx.restore();
            },
            hp: 1, score: 100
        },
        { // Bee
            color: '#ff0',
            draw(x, y, w, h, t) {
                ctx.save(); ctx.translate(x, y);
                ctx.imageSmoothingEnabled = false;
                ctx.shadowColor = this.color;
                ctx.shadowBlur = 5 * scale;
                let spriteName = (Math.floor(t / 10) % 2 === 0) ? 'bee1' : 'bee2';
                let sprite = renderedSprites[spriteName];
                if (sprite) ctx.drawImage(sprite.canvas, -w/2, -h/2, w, h);
                ctx.shadowBlur = 0;
                ctx.restore();
            },
            hp: 1, score: 150
        },
        { // Boss
            color: '#0f0',
            draw(x, y, w, h, t) {
                ctx.save(); ctx.translate(x, y);
                let bw = w * 1.3, bh = h * 1.3;
                ctx.imageSmoothingEnabled = false;
                ctx.shadowColor = this.color;
                ctx.shadowBlur = 8 * scale;
                let spriteName = (Math.floor(t / 20) % 2 === 0) ? 'boss1' : 'boss2';
                let sprite = renderedSprites[spriteName];
                if (sprite) ctx.drawImage(sprite.canvas, -bw/2, -bh/2, bw, bh);
                ctx.shadowBlur = 0;
                ctx.restore();
            },
            hp: 3, score: 400
        },
        { // Stealth - fades in and out
            color: '#88f',
            draw(x, y, w, h, t) {
                ctx.save(); ctx.translate(x, y);
                let alpha = 0.3 + Math.abs(Math.sin(t * 0.03)) * 0.7;
                ctx.globalAlpha = alpha;
                ctx.imageSmoothingEnabled = false;
                ctx.shadowColor = this.color;
                ctx.shadowBlur = 6 * scale;
                let spriteName = (Math.floor(t / 12) % 2 === 0) ? 'stealth1' : 'stealth2';
                let sprite = renderedSprites[spriteName];
                if (sprite) ctx.drawImage(sprite.canvas, -w/2, -h/2, w, h);
                ctx.shadowBlur = 0;
                ctx.globalAlpha = 1;
                ctx.restore();
            },
            hp: 1, score: 250
        },
        { // Bomber
            color: '#f80',
            draw(x, y, w, h, t) {
                ctx.save(); ctx.translate(x, y);
                let bw = w * 1.15, bh = h * 1.15;
                ctx.imageSmoothingEnabled = false;
                ctx.shadowColor = this.color;
                ctx.shadowBlur = 6 * scale;
                let spriteName = (Math.floor(t / 8) % 2 === 0) ? 'bomber1' : 'bomber2';
                let sprite = renderedSprites[spriteName];
                if (sprite) ctx.drawImage(sprite.canvas, -bw/2, -bh/2, bw, bh);
                ctx.shadowBlur = 0;
                ctx.restore();
            },
            hp: 2, score: 300
        }
    ];

"""
content = re.sub(enemy_types_regex, new_enemy_types, content, flags=re.DOTALL)

with open('games/galaga/galaga.html', 'w') as f:
    f.write(content)

print("Patch 4 applied.")
