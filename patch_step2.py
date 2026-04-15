import re

with open('games/galaga/galaga.html', 'r') as f:
    content = f.read()

# Add coinInsert sound
sound_methods_insert = r"// --- SOUND EFFECTS ---"
coin_sound_code = """// --- SOUND EFFECTS ---

        coinInsert() {
            if (!this.ctx) return;
            this.resume();
            const t = this.ctx.currentTime;

            // Arcade coin insert sound: two high-pitched chimes
            this.playTone(987.77, 'square', 0.1, 0.1, t); // B5
            this.playTone(1318.51, 'square', 0.3, 0.1, t + 0.1); // E6
        },"""

content = content.replace(sound_methods_insert, coin_sound_code)

# Replace startBtn event listeners
event_listeners_find = r"""document\.getElementById\('startBtn'\)\.addEventListener\('click', startGame\);
    document\.getElementById\('startBtn'\)\.addEventListener\('touchend', function\(e\) \{ e\.preventDefault\(\); startGame\(\); \}\);
    document\.getElementById\('restartBtn'\)\.addEventListener\('click', startGame\);
    document\.getElementById\('restartBtn'\)\.addEventListener\('touchend', function\(e\) \{ e\.preventDefault\(\); startGame\(\); \}\);"""

new_event_listeners = """
    function handleStartClick(e) {
        if (e) e.preventDefault();

        // Ensure audio context is started on user gesture
        Sound.resume();

        const coinAnim = document.getElementById('coinAnim');
        if (coinAnim && !coinAnim.classList.contains('drop')) {
            Sound.coinInsert();
            coinAnim.classList.add('drop');
            setTimeout(() => {
                coinAnim.classList.remove('drop');
                startGame();
            }, 800); // Wait for animation
        } else if (!coinAnim) {
            startGame();
        }
    }

    document.getElementById('startBtn').addEventListener('click', handleStartClick);
    document.getElementById('startBtn').addEventListener('touchend', handleStartClick);

    // For restart button, just start the game directly
    document.getElementById('restartBtn').addEventListener('click', function(e) { e.preventDefault(); startGame(); });
    document.getElementById('restartBtn').addEventListener('touchend', function(e) { e.preventDefault(); startGame(); });
"""

content = re.sub(event_listeners_find, new_event_listeners.strip(), content, flags=re.MULTILINE)

with open('games/galaga/galaga.html', 'w') as f:
    f.write(content)

print("Patch 2 applied.")
