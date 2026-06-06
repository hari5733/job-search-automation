from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto(
        "https://www.atlassian.com/company/careers",
        wait_until="networkidle"
    )

    print("Title:", page.title())

    page.screenshot(path="atlassian.png")

    input("Press Enter to close browser...")

    browser.close()