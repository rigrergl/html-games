import os
from playwright.sync_api import sync_playwright

def run_cuj(page):
    # Get the absolute path to the HTML file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    html_path = f"file://{current_dir}/gabby-site.html"

    page.goto(html_path)
    page.wait_for_timeout(1000)

    # Hover near the nav bar to attract the cat
    nav_box = page.locator("#navBar").bounding_box()
    if nav_box:
        # Move mouse near the nav bar
        target_x = nav_box['x'] + nav_box['width'] / 2
        target_y = nav_box['y'] + nav_box['height'] / 2

        # Simulate moving the mouse there to trigger the cat walking towards it
        page.mouse.move(target_x, target_y)

        # Wait a few seconds for the cat to walk over and potentially trigger the destruction mechanic
        page.wait_for_timeout(3000)

        # Take a screenshot
        page.screenshot(path="/home/jules/verification/screenshots/verification.png")

        # Wait a bit longer to capture the final state in the video
        page.wait_for_timeout(3000)

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_video_dir="/home/jules/verification/videos"
        )
        page = context.new_page()
        try:
            run_cuj(page)
        finally:
            context.close()
            browser.close()