import glob

keywords = [
    "devops",
    "kubernetes",
    "terraform",
    "aws",
    "cloud"
]

print("Searching Career Pages...\n")

for file in glob.glob("*.html"):

    with open(
        file,
        "r",
        encoding="utf-8",
        errors="ignore"
    ) as f:

        content = f.read().lower()

        found = []

        for keyword in keywords:

            if keyword in content:
                found.append(keyword)

        if found:
            print(
                f"{file} -> {', '.join(found)}"
            )