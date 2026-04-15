import re

with open('games/galaga/galaga.html', 'r') as f:
    content = f.read()

# Add SPRITE_PALETTE and SPRITES and initSprites() right before getViewportHeight()

sprites_code = """    // --- PIXEL ART SPRITES ---
    const SPRITE_PALETTE = {
        '.': null,
        'W': '#ffffff', // White
        'R': '#ff0000', // Red
        'G': '#00ff00', // Green
        'B': '#0000ff', // Blue
        'Y': '#ffff00', // Yellow
        'O': '#ffa500', // Orange
        'C': '#00ffff', // Cyan
        'M': '#ff00ff', // Magenta
        'D': '#555555', // Dark Grey
        'L': '#aaaaaa', // Light Grey
        'P': '#ffb6c1'  // Pink
    };

    const SPRITES = {
        ship: [
            ".......W........",
            "......WWW.......",
            "......WWW.......",
            ".....WWWWW......",
            "....WW.R.WW.....",
            "....WW.W.WW.....",
            "....WW.W.WW.....",
            "....WWWWWWW.....",
            "....WWWWWWW.....",
            "...WWWWWWWWW....",
            "...W.WWWWW.W....",
            "..WW.WWWWW.WW...",
            "..WW.WWWWW.WW...",
            ".WW..WWWWW..WW..",
            ".WW..WWWWW..WW..",
            "WW...WWWWW...WW."
        ],
        shipFlame1: [
            ".......R........",
            "......RYR.......",
            "......YWY.......",
            ".......Y........"
        ],
        shipFlame2: [
            "......RYR.......",
            "......YWY.......",
            ".......W........",
            "................"
        ],
        bug1: [
            "....R....R....",
            ".....R..R.....",
            "....RRRRRR....",
            "...RR.RR.RR...",
            "..RRRRRRRRRR..",
            "..RRRRRRRRRR..",
            "..R.RRRRRR.R..",
            "....R....R...."
        ],
        bug2: [
            "....R....R....",
            ".....R..R.....",
            "....RRRRRR....",
            "...RR.RR.RR...",
            "..RRRRRRRRRR..",
            "..RR.RRRR.RR..",
            "..R.R....R.R..",
            "...R......R..."
        ],
        bee1: [
            "....WWWW....",
            "..WWYWWYWW..",
            "..WWWWWWWW..",
            "..YYYYYYYY..",
            "...YY..YY...",
            "....YYYY....",
            ".....YY.....",
            ".....YY....."
        ],
        bee2: [
            "....WWWW....",
            "..W.YWWY.W..",
            "..WWWWWWWW..",
            "...YYYYYY...",
            "..Y.YY..Y.Y.",
            "....YYYY....",
            "...Y.YY.Y...",
            ".....YY....."
        ],
        boss1: [
            "..GG......GG..",
            "G..G......G..G",
            "G..GGGGGGGG..G",
            "G.GGGGGGGGGG.G",
            ".GGGGGGGGGGGG.",
            ".G.GGGGGGGG.G.",
            ".G.GG....GG.G.",
            "..G........G.."
        ],
        boss2: [
            "..GG......GG..",
            ".G.G......G.G.",
            "G..GGGGGGGG..G",
            ".GGGGGGGGGGGG.",
            ".GGGGGGGGGGGG.",
            "..GGGGGGGGGG..",
            "...GG....GG...",
            "G.G........G.G"
        ],
        stealth1: [
            "......CC......",
            ".....C..C.....",
            "....C....C....",
            "...C......C...",
            "..C........C..",
            "...C......C...",
            "....C....C....",
            ".....CCCC....."
        ],
        stealth2: [
            "......CC......",
            "......CC......",
            ".....CCCC.....",
            "....C....C....",
            "...C......C...",
            "..C........C..",
            "...C......C...",
            "....CCCCCC...."
        ],
        bomber1: [
            "....OOOOOO....",
            "...OOOOOOOO...",
            "..OO.OOOO.OO..",
            ".OOOOOOOOOOOO.",
            ".OO.OOOOOO.OO.",
            ".OOOOOOOOOOOO.",
            "..OO......OO..",
            "O.OO......OO.O"
        ],
        bomber2: [
            "....OOOOOO....",
            "...OOOOOOOO...",
            "..OO.OOOO.OO..",
            ".OOOOOOOOOOOO.",
            "OOO.OOOOOO.OOO",
            ".OOOOOOOOOOOO.",
            "..OO......OO..",
            "...O......O..."
        ]
    };

    let renderedSprites = {};

    function initSprites() {
        for (let key in SPRITES) {
            let art = SPRITES[key];
            let cols = art[0].length;
            let rows = art.length;

            // Create a small offscreen canvas for crisp nearest-neighbor scaling
            let sc = document.createElement('canvas');
            sc.width = cols;
            sc.height = rows;
            let sctx = sc.getContext('2d');
            sctx.imageSmoothingEnabled = false;

            for (let y = 0; y < rows; y++) {
                for (let x = 0; x < cols; x++) {
                    let char = art[y][x];
                    let color = SPRITE_PALETTE[char];
                    if (color) {
                        sctx.fillStyle = color;
                        sctx.fillRect(x, y, 1, 1);
                    }
                }
            }
            renderedSprites[key] = {
                canvas: sc,
                w: cols,
                h: rows
            };
        }
    }

    function getViewportHeight() { return window.innerHeight; }"""

content = content.replace("function getViewportHeight() { return window.innerHeight; }", sprites_code)

# Ensure initSprites is called in resize()
resize_find = """    function resize() {
        W = canvas.width = window.innerWidth;
        H = canvas.height = getViewportHeight();"""

resize_replace = """    function resize() {
        W = canvas.width = window.innerWidth;
        H = canvas.height = getViewportHeight();
        if (Object.keys(renderedSprites).length === 0) {
            initSprites();
        }"""

content = content.replace(resize_find, resize_replace)

with open('games/galaga/galaga.html', 'w') as f:
    f.write(content)

print("Patch 3 applied.")
