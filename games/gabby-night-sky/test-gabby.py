import os
import asyncio
from playwright.async_api import async_playwright

async def main():
    game_dir = os.path.dirname(os.path.abspath(__file__))
    screenshot_path = os.path.join(game_dir, 'screenshot.png')

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # Load the local server
        await page.goto("http://localhost:8080/games/gabby-night-sky/gabby-night-sky.html")
        await page.wait_for_selector('.website-container')

        # Trigger some cat interactions by clicking around
        await page.mouse.click(200, 200)
        await asyncio.sleep(1)

        # Click near the navbar to increase chances of interaction
        await page.mouse.click(500, 50)
        await asyncio.sleep(2)

        # Take screenshot
        await page.screenshot(path=screenshot_path)

        await browser.close()

        print(f"Screenshot saved to {screenshot_path}")

if __name__ == "__main__":
    asyncio.run(main())
