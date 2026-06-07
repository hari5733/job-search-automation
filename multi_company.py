import pandas as pd
import requests

companies = pd.read_csv("companies.csv")

print("Checking Career Sites...\n")

for index, row in companies.iterrows():

    company = row["Company"]
    url = row["URL"]

    try:
        response = requests.get(
            url,
            timeout=10
        )

        print(
            f"{company} -> {response.status_code}"
        )

    except Exception as e:

        print(
            f"{company} -> ERROR"
        )