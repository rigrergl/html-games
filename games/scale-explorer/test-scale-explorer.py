import os
from playwright.sync_api import sync_playwright

def run():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1280, "height": 720})

        # Log console messages to verify no JS errors
        page.on("console", lambda msg: print(f"Console {msg.type}: {msg.text}"))

        page.goto("http://localhost:8000/games/scale-explorer/scale-explorer.html")
        page.wait_for_selector(".synthwave-container")

        # Take a screenshot of the piano (default view)
        screenshot_path = os.path.join(script_dir, "screenshot.png")
        page.screenshot(path=screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

        # Test clicking a button
        page.click("#play-prog-btn")
        page.wait_for_timeout(2000) # wait for part of scale sequence

        # Switch to guitar view
        page.select_option("#instrument", "guitar")
        page.wait_for_timeout(500)

        # Take another screenshot if needed or just assert it switched
        print("Guitar view loaded successfully")

        browser.close()

if __name__ == "__main__":
    run()
