import re

with open('games/galaga/galaga.html', 'r') as f:
    content = f.read()

# Add font-face and apply font
font_css = """
        @font-face {
            font-family: 'Press Start 2P';
            src: url('fonts/PressStart2P.ttf') format('truetype');
        }

        html, body {
            background: #000;
            overflow: hidden;
            touch-action: none;
            position: fixed;
            width: 100%;
            height: 100%;
            font-family: 'Press Start 2P', 'Courier New', monospace;
        }
"""
content = re.sub(r'html, body \{.*?\n        \}', font_css.strip(), content, flags=re.DOTALL)


# Update .btn css and add coin slot CSS
btn_css_find = r'\.btn \{.*?\n        \}'
btn_css_replace = """
        .btn {
            margin-top: 30px;
            padding: 18px 54px;
            font-size: clamp(14px, 4vw, 24px);
            font-family: 'Press Start 2P', monospace;
            background: transparent;
            color: #0f0;
            border: 2px solid #0f0;
            border-radius: 8px;
            cursor: pointer;
            text-shadow: 0 0 10px #0f0;
            box-shadow: 0 0 15px rgba(0,255,0,0.3), inset 0 0 15px rgba(0,255,0,0.1);
        }

        .coin-slot-container {
            margin-top: 40px;
            display: flex;
            flex-direction: column;
            align-items: center;
            cursor: pointer;
            position: relative;
        }

        .insert-coin-text {
            color: #ff0;
            font-size: clamp(12px, 3.5vw, 20px);
            animation: blink 1s step-end infinite;
            margin-bottom: 20px;
            text-shadow: 2px 2px #f00;
        }

        @keyframes blink {
            50% { opacity: 0; }
        }

        .coin-slot {
            width: 40px;
            height: 80px;
            background: #222;
            border: 4px solid #555;
            border-radius: 5px;
            position: relative;
            box-shadow: inset 0 0 10px #000, 0 0 10px rgba(255,255,255,0.2);
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .coin-slot-hole {
            width: 8px;
            height: 50px;
            background: #000;
            border-radius: 4px;
            box-shadow: inset 0 0 5px rgba(255,0,0,0.5);
        }

        .coin {
            position: absolute;
            top: -60px;
            width: 30px;
            height: 30px;
            background: radial-gradient(circle, #ffd700 30%, #b8860b 80%);
            border-radius: 50%;
            border: 2px solid #daa520;
            opacity: 0;
            pointer-events: none;
            box-shadow: 0 0 10px rgba(255,215,0,0.5);
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 10px;
            color: #b8860b;
        }

        .coin::after {
            content: "25¢";
        }

        .coin.drop {
            animation: coinDrop 0.8s ease-in forwards;
        }

        @keyframes coinDrop {
            0% { top: -60px; opacity: 0; transform: scale(1.5) rotateY(0deg); }
            20% { opacity: 1; }
            60% { top: -20px; transform: scale(1) rotateY(360deg); }
            80% { top: 10px; opacity: 1; }
            100% { top: 40px; opacity: 0; transform: scale(0.8) rotateY(720deg); }
        }
"""
content = re.sub(btn_css_find, btn_css_replace.strip(), content, flags=re.DOTALL)

# Replace #startBtn
start_btn_html = r'<button class="btn" id="startBtn">START</button>'
coin_slot_html = """
        <div class="coin-slot-container" id="startBtn">
            <div class="insert-coin-text">INSERT COIN</div>
            <div class="coin-slot">
                <div class="coin-slot-hole"></div>
            </div>
            <div class="coin" id="coinAnim"></div>
        </div>
"""
content = content.replace(start_btn_html, coin_slot_html.strip())


with open('games/galaga/galaga.html', 'w') as f:
    f.write(content)

print("Patch applied successfully.")
