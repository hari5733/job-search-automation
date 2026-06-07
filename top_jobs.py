import pandas as pd

df = pd.read_csv("all_jobs.csv")

top_jobs = df.sort_values(
    by="ATS Score",
    ascending=False
)

top_jobs = top_jobs.head(15)

top_jobs.to_csv(
    "top_jobs.csv",
    index=False
)

print(top_jobs)