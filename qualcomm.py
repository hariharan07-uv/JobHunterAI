import requests

KEYWORDS = [
    "embedded",
    "firmware",
    "linux",
    "android",
    "driver",
    "kernel",
    "hardware",
    "software",
    "integration",
    "nfc",
    "wireless",
    "c++",
    "c "
]

url = "https://careers.qualcomm.com/api/pcsx/search?domain=qualcomm.com"

data = requests.get(url).json()

jobs = data["data"]["positions"]

matches = []

for job in jobs:

    title = job["name"].lower()

    if any(k in title for k in KEYWORDS):

        matches.append({
            "Company": "Qualcomm",
            "Role": job["name"],
            "Location": ", ".join(job["locations"]),
            "Link": f"https://careers.qualcomm.com{job['positionUrl']}"
        })

        print("\n🚀 MATCH FOUND")
        print("Role:", job["name"])
        print("Location:", ", ".join(job["locations"]))

print("\nTotal Qualcomm Jobs:", len(matches))