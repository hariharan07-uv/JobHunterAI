import requests

url = "https://careers.qualcomm.com/api/pcsx/search?domain=qualcomm.com"

r = requests.get(url)

print("Status:", r.status_code)
print(r.text[:2000])