from playwright.sync_api import sync_playwright
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(record_video_dir=".", record_video_size={"width": 800, "height": 600})
        page = context.new_page()
        page.set_viewport_size({"width": 800, "height": 600})

        # Navigate to game
        page.goto("http://localhost:8000/games/galaga/galaga.html")
        time.sleep(1) # wait for fonts/sprites to load

        # Verify font and start screen layout
        page.screenshot(path="games/galaga/screenshot.png")

        # Click the start button (coin slot) to trigger animation
        page.click("#startBtn")
        time.sleep(0.5) # Wait for coin animation mid-drop

        # Wait for game to start
        time.sleep(1)

        # Wait a bit in game to see enemies and bullets
        time.sleep(3)

        # Close
        context.close()
        browser.close()

run()
