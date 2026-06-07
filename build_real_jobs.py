import pandas as pd

files = [
    "atlassian_jobs.csv",
    "adobe_jobs.csv"
]

company_map = {
    "atlassian_jobs.csv": "Atlassian",
    "adobe_jobs.csv": "Adobe"
}

all_jobs = []

for file in files:

    df = pd.read_csv(file)

    company = company_map[file]

    for job in df["Job Title"]:

        all_jobs.append([
            company,
            job
        ])

jobs_df = pd.DataFrame(
    all_jobs,
    columns=[
        "Company",
        "Job Title"
    ]
)

jobs_df.to_csv(
    "real_jobs.csv",
    index=False
)

print(jobs_df.head(20))
print("\nreal_jobs.csv created")