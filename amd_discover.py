import requests

url = "https://careers.amd.com/jobs/search"

r = requests.get(url)

print("Status:", r.status_code)
print(r.url)
print(r.text[:2000])