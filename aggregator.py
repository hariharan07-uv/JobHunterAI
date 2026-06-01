import requests
import pandas as pd

all_jobs = []

# ======================
# BOSCH
# ======================

KEYWORDS = [
    "embedded",
    "firmware",
    "electronics",
    "hardware",
    "pcb",
    "iot",
    "robotics",
    "stm32",
    "esp32",
    "rtos",
    "microcontroller"
]

INDIA_CITIES = [
    "bengaluru",
    "bangalore",
    "coimbatore",
    "chennai",
    "hyderabad",
    "pune",
    "delhi",
    "gurgaon",
    "noida"
]

try:

    url = "https://api.smartrecruiters.com/v1/companies/BoschGroup/postings"

    data = requests.get(url).json()

    for job in data["content"]:

        title = job["name"].lower()

        city = job["location"]["city"].lower()

        if city not in INDIA_CITIES:
            continue

        if any(k in title for k in KEYWORDS):

            all_jobs.append({
                "Company": "Bosch",
                "Role": job["name"],
                "Location": city,
                "Link": f"https://careers.smartrecruiters.com/BoschGroup/{job['id']}"
            })

except Exception as e:
    print("Bosch Error:", e)

# ======================
# GREENHOUSE
# ======================

COMPANIES = [
    "discord",
    "reddit",
    "datadog"
]

try:

    for company in COMPANIES:

        url = f"https://boards-api.greenhouse.io/v1/boards/{company}/jobs"

        data = requests.get(url).json()

        for job in data["jobs"]:

            title = job["title"].lower()

            if any(k in title for k in KEYWORDS):

                all_jobs.append({
                    "Company": company,
                    "Role": job["title"],
                    "Location": "N/A",
                    "Link": job["absolute_url"]
                })

except Exception as e:
    print("Greenhouse Error:", e)

# ======================
# SAVE CSV
# ======================

df = pd.DataFrame(all_jobs)

df.to_csv("all_jobs.csv", index=False)

print(df)

print(f"\nTotal Jobs Found: {len(df)}")
print("Saved as all_jobs.csv")