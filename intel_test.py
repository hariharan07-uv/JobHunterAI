import requests
import json

url = "https://intel.wd1.myworkdayjobs.com/wday/cxs/intel/External/jobs"

payload = {
    "limit": 20,
    "offset": 0,
    "searchText": ""
}

headers = {
    "Content-Type": "application/json"
}

r = requests.post(url, json=payload, headers=headers)

print("Status:", r.status_code)
print(r.text[:1000])
