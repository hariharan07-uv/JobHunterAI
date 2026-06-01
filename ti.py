import requests

url = "https://careers.ti.com/en/sites/CX/jobs?keyword=Embedded"

response = requests.get(url)

print("Status:", response.status_code)

with open("ti.html", "w", encoding="utf-8") as f:
    f.write(response.text)

print("Saved as ti.html")