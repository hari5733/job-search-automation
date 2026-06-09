from bs4 import BeautifulSoup
import pandas as pd

# Read SAP HTML File
with open(
    "sap.html",
    "r",
    encoding="utf-8",
    errors="ignore"
) as f:
    html = f.read()

# Parse HTML
soup = BeautifulSoup(
    html,
    "html.parser"
)

jobs = []

# Extract possible jobs
for text in soup.stripped_strings:

    text = text.strip()

    # Skip long text
    if len(text) > 100:
        continue

    # Job-related keywords
    if (
        "engineer" in text.lower()
        or "manager" in text.lower()
        or "developer" in text.lower()
        or "consultant" in text.lower()
        or "architect" in text.lower()
        or "cloud" in text.lower()
    ):
        jobs.append(text)

# Create DataFrame
df = pd.DataFrame(
    jobs,
    columns=["Job Title"]
)

# Remove duplicates
df.drop_duplicates(
    inplace=True
)

# Save CSV
df.to_csv(
    "sap_jobs.csv",
    index=False
)

# Show Results
print(df.head(20))

print("\nsap_jobs.csv created")