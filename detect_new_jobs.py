import pandas as pd
import os

CURRENT_FILE = "real_jobs.csv"
OLD_FILE = "old_jobs.csv"
NEW_FILE = "new_jobs.csv"

if not os.path.exists(OLD_FILE):

    df = pd.read_csv(CURRENT_FILE)

    df.to_csv(
        OLD_FILE,
        index=False
    )

    print("First run - old_jobs.csv created")

else:

    current = pd.read_csv(CURRENT_FILE)
    old = pd.read_csv(OLD_FILE)

    new_jobs = current[
        ~current["Job Title"].isin(
            old["Job Title"]
        )
    ]

    new_jobs.to_csv(
        NEW_FILE,
        index=False
    )

    current.to_csv(
        OLD_FILE,
        index=False
    )

    print(new_jobs)

    print(
        f"\nNew Jobs Found: {len(new_jobs)}"
    )