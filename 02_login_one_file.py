from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username", exact=True).fill("locked_out_user")
    page.get_by_placeholder("Password", exact=True).fill("secret_sauce")
    page.get_by_role("button", name="Login", exact=True).click()
    warning = page.locator('[data-test="error"]')
    expect(warning).to_have_text(
        "Epic sadface: Sorry, this user has been locked out."
    )
    print("Warning:", warning.inner_text())
    print("PASS: locked account stays on the login screen")
    browser.close()
