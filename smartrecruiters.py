import requests

COMPANIES = [
    "BoschGroup",
    "NXP",
    "Infineon"
]

KEYWORDS = [
    "embedded",
    "firmware",
    "hardware",
    "electronics",
    "pcb",
    "iot",
    "rtos",
    "microcontroller",
    "linux",
    "kernel",
    "driver",
    "fpga",
    "asic"
]

for company in COMPANIES:

    print(f"\nChecking {company}...")

    try:

        url = f"https://api.smartrecruiters.com/v1/companies/{company}/postings"

        data = requests.get(url).json()

        for job in data.get("content", []):

            title = job["name"].lower()

            if any(k in title for k in KEYWORDS):

                print("\n🚀 MATCH FOUND")
                print("Company:", company)
                print("Role:", job["name"])

    except Exception as e:
        print("Error:", e)