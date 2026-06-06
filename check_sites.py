import pandas as pd
import requests

df = pd.read_csv("companies.csv")

for index, row in df.iterrows():
    company = row["Company"]
    url = row["URL"]

    try:
        response = requests.get(url, timeout=10)

        print(f"{company} : {response.status_code}")

    except Exception as e:
        print(f"{company} : ERROR - {e}")