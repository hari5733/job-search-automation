import requests

url = "https://amazon.jobs/en/search?base_query=DevOps"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)

with open("amazon.html", "w", encoding="utf-8") as f:
    f.write(response.text)

print("Page Saved Successfully")