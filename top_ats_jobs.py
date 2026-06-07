import pandas as pd

df = pd.read_csv("ats_results.csv")

top_jobs = df.head(5)

print(top_jobs)

top_jobs.to_csv(
    "top_ats_jobs.csv",
    index=False
)

print("\ntop_ats_jobs.csv created")