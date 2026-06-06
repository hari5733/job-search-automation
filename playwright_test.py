from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto("https://amazon.jobs/en/search?base_query=DevOps")

    print("Title:", page.title())

    page.screenshot(path="amazon_jobs.png")

    input("Press Enter to close browser...")

    browser.close()