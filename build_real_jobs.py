import pandas as pd

files = {
    "atlassian_jobs.csv": "Atlassian",
    "adobe_jobs.csv": "Adobe",
    "servicenow_jobs.csv": "ServiceNow",
    "sap_jobs.csv": "SAP",
    "phonepe_jobs.csv": "PhonePe",
    "postman_jobs.csv": "Postman",
    "razorpay_jobs.csv": "Razorpay",
    "harness_jobs.csv": "Harness"
}

all_jobs = []

for file, company in files.items():

    try:

        df = pd.read_csv(file)

        for job in df["Job Title"]:

            all_jobs.append([
                company,
                job
            ])

    except Exception as e:

        print(f"Skipping {file}: {e}")

jobs_df = pd.DataFrame(
    all_jobs,
    columns=[
        "Company",
        "Job Title"
    ]
)

jobs_df.drop_duplicates(inplace=True)

jobs_df.to_csv(
    "real_jobs.csv",
    index=False
)

print(jobs_df.head(20))
print(f"\nTotal Jobs: {len(jobs_df)}")
print("real_jobs.csv created")