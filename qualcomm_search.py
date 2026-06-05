import requests

url = "https://careers.qualcomm.com"

html = requests.get(url).text

for line in html.split("\n"):

    if "api" in line.lower():
        print(line[:300])

    if "job" in line.lower():
        print(line[:300])