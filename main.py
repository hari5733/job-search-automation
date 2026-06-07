import os

print("STEP 1 - Generate Jobs")
os.system("python generate_jobs.py")

print("\nSTEP 2 - ATS Match")
os.system("python ats_match.py")

print("\nSTEP 3 - Top ATS Jobs")
os.system("python top_ats_jobs.py")

print("\nSTEP 4 - Email Report")
os.system("python email_jobs.py")

print("\nAutomation Completed Successfully")