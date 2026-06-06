with open("amazon.html", "r", encoding="utf-8") as f:
    content = f.read()

if "DevOps" in content:
    print("DevOps Found")
else:
    print("DevOps Not Found")