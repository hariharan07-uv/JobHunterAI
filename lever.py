import requests

COMPANIES = [
    "figma",
    "robinhood",
    "notion",
    "scale-ai",
    "rippling"
]

for company in COMPANIES:

    url = f"https://api.lever.co/v0/postings/{company}?mode=json"

    response = requests.get(url)

    print("\n" + "="*50)
    print(company)
    print("Status:", response.status_code)

    if response.status_code == 200:
        jobs = response.json()
        print("Jobs:", len(jobs))