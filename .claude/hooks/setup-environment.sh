#!/bin/bash
# SessionStart hook: sets up the browser environment for HTML game development.
# This runs automatically when Claude Code starts in this project.

CHROME_DIR="/opt/chrome-for-testing/chrome-linux64"
CHROME_BIN="$CHROME_DIR/chrome"
PROJECT_DIR="${CLAUDE_PROJECT_DIR:-/home/user/html-games}"

# Step 1: Install Chrome for Testing if not present
if [ ! -f "$CHROME_BIN" ]; then
    echo "[setup] Downloading Chrome for Testing..."
    curl -sL --max-time 120 "https://storage.googleapis.com/chrome-for-testing-public/131.0.6778.85/linux64/chrome-linux64.zip" -o /tmp/chrome.zip
    mkdir -p /opt/chrome-for-testing
    unzip -qo /tmp/chrome.zip -d /opt/chrome-for-testing
    rm -f /tmp/chrome.zip
    echo "[setup] Chrome for Testing installed at $CHROME_BIN"
else
    echo "[setup] Chrome for Testing already installed."
fi

# Step 2: Install MCP server packages (skip if already installed)
if ! command -v chrome-devtools-mcp &>/dev/null || ! npx @playwright/mcp --version &>/dev/null; then
    echo "[setup] Installing MCP server packages..."
    npm install -g @playwright/mcp@latest 2>/dev/null || true
    npm install -g chrome-devtools-mcp@latest 2>/dev/null || true
else
    echo "[setup] MCP server packages already installed."
fi

# Step 3: Kill any existing Chrome debug instances
pkill -f "chrome.*remote-debugging-port=9222" 2>/dev/null || true
sleep 1

# Step 4: Launch Chrome in headless mode with CDP
echo "[setup] Launching headless Chrome with CDP on port 9222..."
nohup "$CHROME_BIN" \
    --headless=new \
    --no-sandbox \
    --disable-gpu \
    --disable-dev-shm-usage \
    --remote-debugging-port=9222 \
    --window-size=1280,720 \
    &>/dev/null &

sleep 2

# Step 5: Verify Chrome is running
if curl -s http://localhost:9222/json/version > /dev/null 2>&1; then
    echo "[setup] Chrome CDP is running on port 9222."
else
    echo "[setup] WARNING: Chrome CDP failed to start. MCP servers may not connect."
fi

# Step 6: Start local HTTP server for serving game files
pkill -f "python3 -m http.server 8080" 2>/dev/null || true
sleep 0.5
cd "$PROJECT_DIR"
nohup python3 -m http.server 8080 &>/dev/null &
echo "[setup] HTTP server running on port 8080."

echo "[setup] Environment ready! MCP servers will connect to Chrome via CDP."
