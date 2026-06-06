import pandas as pd

df = pd.read_csv("companies.csv")

print("Companies to Check:\n")

for index, row in df.iterrows():
    print(f"{row['Company']} -> {row['URL']}")

print("\nAutomation Started Successfully")