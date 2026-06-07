import pandas as pd

jobs = pd.read_csv("top_ats_jobs.csv")

print("\nTOP ATS JOBS TODAY\n")

for _, row in jobs.iterrows():

    print(
        f"{row['ATS Score']}% | "
        f"{row['Company']} | "
        f"{row['Job Title']}"
    )