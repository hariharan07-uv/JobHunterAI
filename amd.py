import requests

s = requests.Session()

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json",
    "Referer": "https://careers.amd.com/careers-home/jobs/search"
}

r = s.get(
    "https://careers.amd.com/api/jobs",
    headers=headers,
    timeout=20
)

print(r.status_code)
print(r.text[:500])