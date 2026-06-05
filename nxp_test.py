import requests

companies = [
    "NXPsemiconductors",
    "NXPSemiconductors",
    "NXPUSA"
]

for company in companies:

    url = f"https://api.smartrecruiters.com/v1/companies/{company}/postings"

    r = requests.get(url)

    try:
        jobs = len(r.json().get("content", []))
    except:
        jobs = "ERROR"

    print(company, "->", jobs)