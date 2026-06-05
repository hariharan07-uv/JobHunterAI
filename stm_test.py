import requests

r = requests.get(
    "https://careers.st.com"
)

print(r.status_code)
print(r.text[:1000])