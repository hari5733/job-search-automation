from bs4 import BeautifulSoup

with open("amazon.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

print("Page Title:")
print(soup.title.text if soup.title else "No Title")

print("\nFirst 20 Links:")

count = 0
for link in soup.find_all("a"):
    text = link.get_text(strip=True)

    if text:
        print(text)
        count += 1

    if count >= 20:
        break