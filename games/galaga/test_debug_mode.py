import os
from playwright.sync_api import sync_playwright

def run_test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Using a context with a fake storage
        context = browser.new_context()
        page = context.new_page()

        # Test 1: Debug mode active - High score should not be saved AND lives should not decrement
        file_path = f"file://{os.path.abspath('games/galaga/galaga.html')}?&debug=true"

        # We inject a script before anything loads to hook localStorage
        page.add_init_script("""
            window._setItemCalled = false;
            const origSetItem = Storage.prototype.setItem;
            Storage.prototype.setItem = function(key, value) {
                if (key === 'galagaHi') {
                    window._setItemCalled = true;
                }
                return origSetItem.call(this, key, value);
            };
        """)

        page.goto(file_path)

        page.evaluate("localStorage.clear(); localStorage.setItem('galagaHi', '0'); window._setItemCalled = false;")

        # Start game
        page.click('#startBtn')
        page.wait_for_timeout(1000)

        print("Playing game...")

        initial_lives_text = page.locator('#lives').inner_text()
        print(f"Initial lives in debug mode: {initial_lives_text}")

        for _ in range(5):
            page.click('#debugUse', timeout=1000)
            page.wait_for_timeout(100)

        for _ in range(100):
            page.keyboard.press(" ")
            page.wait_for_timeout(50)

        print("Waiting for some time to be hit...")
        page.wait_for_timeout(10000)

        lives_text_after_hit = page.locator('#lives').inner_text()
        print(f"Lives after getting hit in debug mode: {lives_text_after_hit}")

        assert lives_text_after_hit == initial_lives_text, "Lives SHOULD NOT decrement in debug mode"
        print("Debug mode lives test passed!")

        # We cannot verify score saving here easily because the game won't end (lives never reach 0)

        context.close()

        # Test 2: Normal mode - High score SHOULD be saved AND lives SHOULD decrement
        context = browser.new_context()
        page = context.new_page()
        file_path_normal = f"file://{os.path.abspath('games/galaga/galaga.html')}"

        page.add_init_script("""
            window._setItemCalled = false;
            const origSetItem = Storage.prototype.setItem;
            Storage.prototype.setItem = function(key, value) {
                if (key === 'galagaHi') {
                    window._setItemCalled = true;
                }
                return origSetItem.call(this, key, value);
            };
        """)

        page.goto(file_path_normal)
        page.evaluate("localStorage.clear(); localStorage.setItem('galagaHi', '0'); window._setItemCalled = false;")

        page.click('#startBtn')
        page.wait_for_timeout(1000)

        initial_lives_text_normal = page.locator('#lives').inner_text()
        print(f"Initial lives in normal mode: {initial_lives_text_normal}")

        print("Playing game in normal mode...")
        for _ in range(100):
            page.keyboard.press(" ")
            page.wait_for_timeout(50)

        page.wait_for_selector('#gameOverScreen', state='visible', timeout=60000)

        lives_text_after_hit_normal = page.locator('#lives').inner_text()
        print(f"Lives after death in normal mode: {lives_text_after_hit_normal}")

        assert lives_text_after_hit_normal != initial_lives_text_normal, "Lives SHOULD decrement in normal mode"

        set_item_called_normal = page.evaluate("window._setItemCalled")
        saved_score_normal = page.evaluate("localStorage.getItem('galagaHi')")

        final_score_text_normal = page.locator('#finalScore').inner_text()
        final_score_normal = int(final_score_text_normal.replace('SCORE: ', '').replace(',', ''))

        print(f"Normal Mode - Final Score: {final_score_normal}")
        print(f"Normal Mode - Set Item Called: {set_item_called_normal}")
        print(f"Normal Mode - Saved Score: {saved_score_normal}")

        if final_score_normal > 0:
            assert set_item_called_normal, "localStorage.setItem SHOULD be called in normal mode"
            assert int(saved_score_normal) == final_score_normal, "High score SHOULD be saved in normal mode"
            print("Normal mode test passed!")
        else:
            print("Warning: Score was 0 in normal mode, could not verify saving.")

        browser.close()

if __name__ == "__main__":
    run_test()
