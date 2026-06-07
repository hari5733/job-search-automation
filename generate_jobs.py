import pandas as pd

jobs = pd.read_csv("jobs.csv")

results = []

for job in jobs["Job Title"]:

    score = 0

    title = str(job).lower()

    keywords = {
        "devops": 30,
        "aws": 20,
        "kubernetes": 25,
        "terraform": 20,
        "jenkins": 15,
        "docker": 15,
        "linux": 15,
        "python": 15,
        "gcp": 15,
        "azure": 15,
        "engineer": 10,
        "cloud": 15,
        "platform": 15,
        "reliability": 15,
        "sre": 20
    }

    for keyword, points in keywords.items():
        if keyword in title:
            score += points

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