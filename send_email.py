import smtplib
from email.message import EmailMessage
import pandas as pd

# Gmail Details
EMAIL = "boyya.awsdevops777@gmail.com"
APP_PASSWORD = "APP_PASSWORD = "REPLACE_WITH_NEW_APP_PASSWORD""

# Read ATS Jobs
jobs = pd.read_csv("top_ats_jobs.csv")

body = "TOP ATS JOBS TODAY\n\n"

for _, row in jobs.iterrows():
    body += (
        f"{row['ATS Score']}% | "
        f"{row['Company']} | "
        f"{row['Job Title']}\n"
    )

# Create Email
msg = EmailMessage()

msg["Subject"] = "Daily ATS Job Report"
msg["From"] = EMAIL
msg["To"] = EMAIL

msg.set_content(body)

# Attach CSV File
with open("top_ats_jobs.csv", "rb") as f:
    msg.add_attachment(
        f.read(),
        maintype="application",
        subtype="octet-stream",
        filename="top_ats_jobs.csv"
    )

# Attach Resume
with open("BOYYA.docx", "rb") as f:
    msg.add_attachment(
        f.read(),
        maintype="application",
        subtype="vnd.openxmlformats-officedocument.wordprocessingml.document",
        filename="BOYYA.docx"
    )

# Send Email
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:

    smtp.login(
        EMAIL,
        APP_PASSWORD
    )

    smtp.send_message(msg)

print("Email Sent Successfully")