import requests

urls = [
    "https://careers.amd.com/jobs",
    "https://careers.amd.com/api/jobs",
    "https://careers.amd.com/jobs/search",
]

for url in urls:

    try:
        r = requests.get(url)

        print("\nURL:", url)
        print("Status:", r.status_code)
        print(r.text[:300])

    except Exception as e:
        print(e)