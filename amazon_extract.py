from playwright.sync_api import sync_playwright
import csv

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    page.goto(
        "https://amazon.jobs/en/search?base_query=DevOps",
        wait_until="networkidle"
    )

    page.wait_for_timeout(5000)

    links = page.locator("a").all_text_contents()

    jobs = []

    for item in links:
        item = item.strip()

        if "DevOps" in item or "Engineer" in item or "Analyst" in item:
            print(item)
            jobs.append(item)

    browser.close()

with open("jobs.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Job Title"])

    for job in jobs:
        writer.writerow([job])

print("Jobs saved to jobs.csv")