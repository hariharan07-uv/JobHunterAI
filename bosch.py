import requests

KEYWORDS = [
    "embedded",
    "firmware",
    "electronics",
    "hardware",
    "pcb",
    "iot",
    "robotics",
    "stm32",
    "esp32",
    "rtos",
    "microcontroller"
]

BLOCKED_WORDS = [
    "frontend",
    "backend",
    "full stack",
    "ios",
    "android",
    "sales",
    "marketing",
    "finance",
    "hr"
]

INDIA_CITIES = [
    "bengaluru",
    "bangalore",
    "coimbatore",
    "chennai",
    "hyderabad",
    "pune",
    "delhi",
    "gurgaon",
    "noida"
]

url = "https://api.smartrecruiters.com/v1/companies/BoschGroup/postings"

response = requests.get(url)

print("Status:", response.status_code)

if response.status_code == 200:

    data = response.json()

    for job in data["content"]:

        title = job["name"].lower()

        city = job["location"]["city"].lower()

        if city not in INDIA_CITIES:
            continue

        if (
            any(k in title for k in KEYWORDS)
            and not any(b in title for b in BLOCKED_WORDS)
        ):

            print("\n🚀 MATCH FOUND")
            print("Role:", job["name"])
            print("Location:", job["location"]["city"])
            print(
                "Link:",
                f"https://careers.smartrecruiters.com/BoschGroup/{job['id']}"
            )