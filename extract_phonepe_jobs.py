from bs4 import BeautifulSoup
import pandas as pd

with open(
    "phonepe.html",
    "r",
    encoding="utf-8",
    errors="ignore"
) as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

jobs = []

for text in soup.stripped_strings:

    text = text.strip()

    if len(text) > 100:
        continue

    if (
        "engineer" in text.lower()
        or "manager" in text.lower()
        or "developer" in text.lower()
        or "analyst" in text.lower()
        or "architect" in text.lower()
        or "devops" in text.lower()
    ):
        jobs.append(text)

df = pd.DataFrame(
    list(set(jobs)),
    columns=["Job Title"]
)

df.to_csv(
    "phonepe_jobs.csv",
    index=False
)

print(df.head(20))
print("\nphonepe_jobs.csv created")