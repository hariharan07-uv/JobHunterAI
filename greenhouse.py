import requests

# Companies to check
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
    "electrical",
    "microcontroller",
    "rtos",
    "automotive",
    "validation engineer",
    "test engineer"
]
print("=" * 60)
print("JOB HUNTER AI")
print("=" * 60)

total_matches = 0

for company in COMPANIES:

    print(f"\nChecking {company}...")

    url = f"https://boards-api.greenhouse.io/v1/boards/{company}/jobs"

    try:

        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            print(f"Failed: {response.status_code}")
            continue

        data = response.json()

        for job in data["jobs"]:

            title = job["title"].lower()

            if any(keyword in title for keyword in KEYWORDS):

                total_matches += 1

                print("\n" + "-" * 60)
                print("COMPANY :", company.upper())
                print("ROLE    :", job["title"])
                print("LINK    :", job["absolute_url"])
                print("-" * 60)

    except Exception as e:
        print(f"Error: {e}")

print("\n")
print("=" * 60)
print(f"TOTAL MATCHES FOUND: {total_matches}")
print("=" * 60)