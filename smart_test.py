import requests

companies = [
    "BoschGroup",
    "NXP",
    "Infineon"
]

for company in companies:

    print(f"\nChecking {company}")

    url = f"https://api.smartrecruiters.com/v1/companies/{company}/postings"

    r = requests.get(url)

    print("Status:", r.status_code)

    try:
        data = r.json()
        print("Jobs:", len(data.get("content", [])))
    except:
        print("Could not parse JSON")