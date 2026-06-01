import requests
import pandas as pd

COMPANIES = [
    "stripe",
    "mongodb",
    "datadog",
    "reddit",
    "hubspot",
    "discord"
]

KEYWORDS = [
    "embedded",
    "firmware",
    "hardware",
    "electronics",
    "robotics",
    "iot",
    "pcb",
    "fpga",
    "electrical"
]

jobs_list = []

for company in COMPANIES:

    url = f"https://boards-api.greenhouse.io/v1/boards/{company}/jobs"

    try:

        data = requests.get(url).json()

        for job in data["jobs"]:

            title = job["title"].lower()

            if any(keyword in title for keyword in KEYWORDS):

                jobs_list.append({
                    "Company": company,
                    "Role": job["title"],
                    "Link": job["absolute_url"]
                })

    except:
        pass

df = pd.DataFrame(jobs_list)

df.to_csv("jobs.csv", index=False)

print(df)
print("\nSaved to jobs.csv")