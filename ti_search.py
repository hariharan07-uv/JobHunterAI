import requests

url = (
    "https://edbz.fa.us2.oraclecloud.com/"
    "hcmRestApi/resources/11.13.18.05/"
    "recruitingCEJobRequisitions"
    "?SiteNumber=CX"
)

response = requests.get(url)

print("Status:", response.status_code)
print(response.text[:3000])