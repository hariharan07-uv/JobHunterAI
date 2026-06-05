import requests

url = "https://careers.amd.com/api/jobs"

params = {
    "keywords": "embedded",
    "sortBy": "relevance",
    "page": 1,
    "internal": "false"
}

r = requests.get(url, params=params)

print("Status:", r.status_code)
print(r.text[:2000])