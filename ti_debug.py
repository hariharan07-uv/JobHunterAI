import requests
import re

url = "https://careers.ti.com/en/sites/CX/jobs?keyword=Embedded"

html = requests.get(url).text

for keyword in [
    "api",
    "requisition",
    "search",
    "jobs",
    "phApp",
    "__INITIAL_STATE__"
]:
    print(f"\nChecking: {keyword}")
    matches = re.findall(f".{{0,100}}{keyword}.{{0,100}}", html, re.IGNORECASE)
    
    for m in matches[:5]:
        print(m)