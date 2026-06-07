import pandas as pd
import requests

companies = pd.read_csv("companies.csv")

for index, row in companies.iterrows():

    company = row["Company"]
    url = row["URL"]

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:

            filename = (
                company.lower()
                + ".html"
            )

            with open(
                filename,
                "w",
                encoding="utf-8"
            ) as file:

                file.write(
                    response.text
                )

            print(
                f"{company} page saved"
            )

    except:
        print(
            f"{company} failed"
        )