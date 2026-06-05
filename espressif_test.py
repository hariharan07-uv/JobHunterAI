import requests

r = requests.get(
    "https://www.espressif.com/en/company/careers"
)

print(r.status_code)
print(r.text[:1000])