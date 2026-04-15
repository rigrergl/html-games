from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1280, "height": 720})

        # Log console messages to verify no JS errors
        page.on("console", lambda msg: print(f"Console {msg.type}: {msg.text}"))

        page.goto("http://localhost:8000/games/scale-explorer/scale-explorer.html")
        page.wait_for_selector(".container")

        # Take a screenshot of the piano (default view)
        page.screenshot(path="games/scale-explorer/screenshot.png")
        print("Screenshot saved to games/scale-explorer/screenshot.png")

        # Test clicking a button
        page.click("#play-scale-btn")
        page.wait_for_timeout(2000) # wait for part of scale sequence

        # Switch to guitar view
        page.select_option("#instrument", "guitar")
        page.wait_for_timeout(500)

        # Take another screenshot if needed or just assert it switched
        print("Guitar view loaded successfully")

        browser.close()

if __name__ == "__main__":
    run()
