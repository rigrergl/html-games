const fs = require('fs');
const content = fs.readFileSync('games/galaga/galaga.html', 'utf8');
const jsMatch = content.match(/<script>([\s\S]*)<\/script>/);
if (jsMatch && jsMatch[1]) {
    try {
        new Function(jsMatch[1]);
        console.log("Syntax OK");
    } catch (e) {
        console.error("Syntax Error:", e);
    }
}
