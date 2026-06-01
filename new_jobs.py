import requests

COMPANIES = [
    "discord",
    "datadog",
    "reddit",
    "hubspot",
    "mongodb",
    "stripe"
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
    "microcontroller",
    "rtos"
]

BLOCKED_WORDS = [
    "android",
    "ios",
    "machine learning",
    "frontend",
    "backend",
    "full stack",
    "software engineer"
]

# Load already-seen jobs
try:
    with open("seen_jobs.txt", "r") as f:
        seen_jobs = set(f.read().splitlines())
except:
    seen_jobs = set()

new_found = False

for company in COMPANIES:

    url = f"https://boards-api.greenhouse.io/v1/boards/{company}/jobs"

    try:
        data = requests.get(url).json()

        for job in data["jobs"]:

            title = job["title"].lower()

            if (
                any(k in title for k in KEYWORDS)
                and not any(b in title for b in BLOCKED_WORDS)
            ):

                job_id = str(job["id"])

                if job_id not in seen_jobs:

                    print("\n🚀 NEW JOB FOUND")
                    print("Company:", company)
                    print("Role:", job["title"])
                    print("Link:", job["absolute_url"])

                    with open("seen_jobs.txt", "a") as f:
                        f.write(job_id + "\n")

                    new_found = True

    except Exception as e:
        print(e)

if not new_found:
    print("No new jobs found.")
