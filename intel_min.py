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
    "limit": 5,
    "searchText": ""
}

r = requests.post(url, json=payload)

data = r.json()

matches = []

for job in data["jobPostings"]:

    title = job["title"].lower()

    if any(keyword in title for keyword in KEYWORDS):

        matches.append(job)

        print("🚀", job["title"])

print("\nTotal Intel Jobs:", len(matches))