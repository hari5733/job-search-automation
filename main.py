import pandas as pd

companies = pd.read_csv("companies.csv")

print("Companies Loaded:", len(companies))

jobs = pd.read_csv("all_jobs.csv")

print("\nTop Jobs:\n")

jobs = jobs.sort_values("ATS Score", ascending=False)

print(jobs)