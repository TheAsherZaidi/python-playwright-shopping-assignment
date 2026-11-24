from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    print("Page title:", page.title())
    page.screenshot(path="01_login_page.png")
    page.wait_for_timeout(10_000) #keep the page visible for 10 seconds.
    browser.close()

