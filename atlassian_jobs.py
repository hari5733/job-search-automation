from bs4 import BeautifulSoup

with open("atlassian.html","r",encoding="utf-8",errors="ignore") as f:
    html = f.read()

soup = BeautifulSoup(html,"html.parser")

for line in soup.stripped_strings:

    text = line.strip()

    if (
        "engineer" in text.lower()
        or "cloud" in text.lower()
        or "platform" in text.lower()
        or "devops" in text.lower()
    ):

        print(text)