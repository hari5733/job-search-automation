from bs4 import BeautifulSoup
import pandas as pd

# Read HTML file
with open(
    "atlassian.html",
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

# Employee names to skip
skip_names = [
    "Sean",
    "Pooja",
    "Dipika",
    "Apurva",
    "Aditya",
    "Niraj",
    "Belto",
    "Tiffany",
    "Martin",
    "Bianca"
]

# Extract possible jobs
for text in soup.stripped_strings:

    text = text.strip()

    # Skip long paragraphs
    if len(text) > 80:
        continue

    # Skip employee names
    if any(name in text for name in skip_names):
        continue

    # Keep only job-like entries
    if (
        "," in text
        and (
            "engineer" in text.lower()
            or "manager" in text.lower()
            or "devops" in text.lower()
            or "cloud" in text.lower()
        )
    ):

        jobs.append(text)

# Create DataFrame
df = pd.DataFrame(
    jobs,
    columns=["Job Title"]
)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Save CSV
df.to_csv(
    "atlassian_jobs.csv",
    index=False
)

# Display results
print(df)

print("\natlassian_jobs.csv created successfully")