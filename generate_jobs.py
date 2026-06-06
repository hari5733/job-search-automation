import pandas as pd

jobs = pd.read_csv("jobs.csv")

results = []

for job in jobs["Job Title"]:

    score = 0

    title = str(job).lower()

    if "devops" in title:
        score += 50

    if "aws" in title:
        score += 20

    if "engineer" in title:
        score += 20

    if "platform" in title:
        score += 10

    results.append([
        "Amazon",
        job,
        score
    ])

df = pd.DataFrame(
    results,
    columns=["Company", "Job Title", "ATS Score"]
)

df.to_csv("all_jobs.csv", index=False)

print("all_jobs.csv generated successfully")