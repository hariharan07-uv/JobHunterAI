import requests

url = "https://edbz.fa.us2.oraclecloud.com/hcmRestApi/resources/11.13.18.05/recruitingCEJobRequisitions/describe"

data = requests.get(url).json()

attrs = data["Resources"]["recruitingCEJobRequisitions"]["attributes"]

for attr in attrs:
    if attr.get("queryable"):
        print(attr["name"])