import requests

url = input("URL: ")

r = requests.get(url)

print("Status:", r.status_code)
print(r.text[:1000])