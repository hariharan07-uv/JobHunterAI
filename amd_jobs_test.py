import requests

url = "https://careers.amd.com/jobs"

r = requests.get(url)

print("Status:", r.status_code)

for keyword in [
    "api",
    "search",
    "jobs",
    "job",
    "position",
    "requisition"
]:
    if keyword.lower() in r.text.lower():
        print("Found:", keyword)