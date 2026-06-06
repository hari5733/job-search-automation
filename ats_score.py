import pandas as pd

my_skills = [
    "AWS",
    "Docker",
    "Kubernetes",
    "Terraform",
    "Jenkins",
    "Python",
    "Linux",
    "Git",
    "DevOps"
]

df = pd.read_csv("jobs.csv")

print("\nATS Match Results\n")

for job in df["Job Title"]:

    score = 0

    for skill in my_skills:
        if skill.lower() in str(job).lower():
            score += 10

    if score > 100:
        score = 100

    print(f"{job} --> {score}%")