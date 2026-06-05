import requests

url = "https://careers.amd.com/api/jobs"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://careers.amd.com/careers-home/jobs/search",
    "Accept": "application/json"
}

try:
    r = requests.get(url, headers=headers, timeout=15)

    print("Status:", r.status_code)

    data = r.json()

    print("Keys:", data.keys())

    jobs = data.get("jobs", [])

    print("Jobs returned:", len(jobs))

    for job in jobs[:5]:
        print(job["data"]["title"])

except Exception as e:
    print("ERROR:", e)