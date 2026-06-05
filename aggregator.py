import requests
import pandas as pd

all_jobs = []

# ======================
# BOSCH
# ======================

KEYWORDS = [
    "embedded",
    "firmware",
    "hardware",
    "electronics",
    "pcb",
    "iot",
    "robotics",
    "stm32",
    "esp32",
    "rtos",
    "microcontroller",
    "linux",
    "kernel",
    "driver",
    "device driver",
    "c++",
    "c ",
    "validation",
    "verification",
    "fpga",
    "asic",
    "signal",
    "automotive"
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
# ======================
# SMARTRECRUITERS
# ======================

SMARTRECRUITER_COMPANIES = [
    ("BoschGroup", "Bosch"),
    ("NXP", "NXP"),
    ("Infineon", "Infineon")
]

for company_id, company_name in SMARTRECRUITER_COMPANIES:

    try:

        url = f"https://api.smartrecruiters.com/v1/companies/{company_id}/postings"

        data = requests.get(url).json()

        for job in data.get("content", []):

            title = job["name"].lower()

            city = job["location"]["city"].lower()

            if city not in INDIA_CITIES:
                continue

            if any(k in title for k in KEYWORDS):

                all_jobs.append({
                    "Company": company_name,
                    "Role": job["name"],
                    "Location": city,
                    "Link": f"https://careers.smartrecruiters.com/{company_id}/{job['id']}"
                })

    except Exception as e:
        print(f"{company_name} Error:", e)

# ======================
# QUALCOMM
# ======================

try:

    url = "https://careers.qualcomm.com/api/pcsx/search?domain=qualcomm.com"

    data = requests.get(url).json()

    for job in data["data"]["positions"]:

        title = job["name"].lower()

        if any(k in title for k in KEYWORDS):

            all_jobs.append({
                "Company": "Qualcomm",
                "Role": job["name"],
                "Location": ", ".join(job["locations"]),
                "Link": f"https://careers.qualcomm.com{job['positionUrl']}"
            })

except Exception as e:
    print("Qualcomm Error:", e)
# ======================
# INTEL
# ======================

try:

    url = "https://intel.wd1.myworkdayjobs.com/wday/cxs/intel/External/jobs"

    payload = {
        "appliedFacets": {},
        "limit": 5,
        "searchText": ""
    }

    data = requests.post(url, json=payload).json()

    for job in data["jobPostings"]:

        title = job["title"].lower()

        if any(keyword in title for keyword in KEYWORDS):

            all_jobs.append({
                "Company": "Intel",
                "Role": job["title"],
                "Location": job["locationsText"],
                "Link": "https://jobs.intel.com" + job["externalPath"]
            })

except Exception as e:
    print("Intel Error:", e)
print("Intel checking:", title)

if any(keyword in title for keyword in KEYWORDS):
    print("Intel MATCH:", job["title"])
# ======================
# SAVE CSV
# ======================
print("Bosch jobs:", len(all_jobs))
df = pd.DataFrame(all_jobs)

df.to_csv("all_jobs.csv", index=False)

print(df)

print(f"\nTotal Jobs Found: {len(df)}")
print("Saved as all_jobs.csv")

print("\n===== SUMMARY =====")

for company in df["Company"].value_counts().items():
    print(company)