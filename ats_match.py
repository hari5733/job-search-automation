import pandas as pd

# Resume Skills
resume_skills = {
    "aws": 20,
    "terraform": 20,
    "kubernetes": 25,
    "docker": 15,
    "jenkins": 15,
    "ansible": 15,
    "python": 15,
    "gcp": 15,
    "azure": 15,
    "cloud": 10,
    "engineer": 5,
    "manager": 5,
    "linux": 10,
    "devops": 20
}

# Preferred DevOps Roles
preferred_roles = [
    "devops",
    "cloud engineer",
    "site reliability",
    "sre",
    "platform engineer",
    "kubernetes",
    "terraform"
]

# DevOps Keywords
devops_keywords = [
    "devops",
    "cloud",
    "engineer",
    "platform",
    "sre",
    "site reliability",
    "kubernetes",
    "terraform",
    "aws",
    "docker",
    "jenkins",
    "ansible",
    "linux"
]

# Remove unwanted entries
bad_keywords = [
    "blog",
    "academy",
    "forbes",
    "developer hub",
    "assessment",
    "for developers",
    "careers at"
]

# Read Jobs
jobs = pd.read_csv("real_jobs.csv")

results = []

for _, row in jobs.iterrows():

    title = str(row["Job Title"]).lower()

    # Skip junk entries
    if any(bad in title for bad in bad_keywords):
        continue

    # Keep only DevOps related jobs
    if not any(keyword in title for keyword in devops_keywords):
        continue

    score = 0

    # Preferred Role Bonus
    for role in preferred_roles:
        if role in title:
            score += 20

    # Resume Skill Matching
    for skill, points in resume_skills.items():
        if skill in title:
            score += points

    results.append([
        row["Company"],
        row["Job Title"],
        score
    ])

# Create DataFrame
df = pd.DataFrame(
    results,
    columns=[
        "Company",
        "Job Title",
        "ATS Score"
    ]
)

# Sort by ATS Score
df = df.sort_values(
    by="ATS Score",
    ascending=False
)

# Save CSV
df.to_csv(
    "ats_results.csv",
    index=False
)

# Display Results
print(df)

print("\nats_results.csv created")