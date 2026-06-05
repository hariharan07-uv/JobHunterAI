import requests

KEYWORDS = [
    "rtl",
    "cpu",
    "soc",
    "silicon",
    "post-silicon",
    "analog",
    "mixed signal",
    "firmware",
    "embedded",
    "hardware",
    "fpga",
    "asic",
    "verification",
    "validation",
    "linux",
    "driver",
    "kernel",
    "physical design"
]

url = "https://intel.wd1.myworkdayjobs.com/wday/cxs/intel/External/jobs"

payload = {
    "appliedFacets": {},
    "limit": 100,
    "searchText": ""
}

r = requests.post(url, json=payload)

data = r.json()
print("Status:", r.status_code)
print("Keys:", data.keys())
print(data)
exit()
matches = []

for job in data["jobPostings"]:

    title = job["title"].lower()

    if any(keyword in title for keyword in KEYWORDS):

        matches.append({
            "Company": "Intel",
            "Role": job["title"],
            "Location": job["locationsText"],
            "Link": "https://jobs.intel.com" + job["externalPath"]
        })

        print("🚀", job["title"])

print("\nTotal Intel Jobs:", len(matches))