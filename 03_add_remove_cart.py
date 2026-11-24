from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    try:
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/")
        
        page.get_by_placeholder("Username", exact=True).fill("standard_user") # change username.
        page.get_by_placeholder("Password", exact=True).fill("secret_sauce")
        page.get_by_role("button", name="Login", exact=True).click()
        
        page.wait_for_timeout(5_000)
        page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
        page.wait_for_timeout(5_000)
        page.locator('[data-test="add-to-cart-sauce-labs-bike-light"]').click()
        page.wait_for_timeout(5_000)
        
        cart_count = page.locator('[data-test="shopping-cart-badge"]')
        expect(cart_count).to_have_text("2")
        page.wait_for_timeout(5_000)
        
        page.locator('[data-test="remove-sauce-labs-bike-light"]').click()
        expect(cart_count).to_have_text("1")
        page.wait_for_timeout(5_000)
        
        page.locator('[data-test="shopping-cart-link"]').click()
        page.wait_for_timeout(5_000)
        expect(page.get_by_text("Sauce Labs Backpack", exact=True)).to_be_visible()
        expect(page.get_by_text("Sauce Labs Bike Light", exact=True)).to_have_count(0)
        
        
        page.screenshot(path="03_add_remove_cart.png")
        print("PASS")
        page.wait_for_timeout(10_000)
        
    finally:
        browser.close()

