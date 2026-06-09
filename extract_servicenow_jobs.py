from bs4 import BeautifulSoup
import pandas as pd

with open(
    "servicenow.html",
    "r",
    encoding="utf-8",
    errors="ignore"
) as f:
    html = f.read()

soup = BeautifulSoup(
    html,
    "html.parser"
)

jobs = []

for text in soup.stripped_strings:

    text = text.strip()

    if len(text) > 80:
        continue

    if (
        "engineer" in text.lower()
        or "manager" in text.lower()
        or "developer" in text.lower()
        or "devops" in text.lower()
        or "cloud" in text.lower()
    ):
        jobs.append(text)

df = pd.DataFrame(
    jobs,
    columns=["Job Title"]
)

df.drop_duplicates(inplace=True)

df.to_csv(
    "servicenow_jobs.csv",
    index=False
)

print(df.head(20))
print("\nservicenow_jobs.csv created")