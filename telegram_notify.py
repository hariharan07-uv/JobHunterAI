import os
import requests
import pandas as pd

BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

df = pd.read_csv("all_jobs.csv")

message = "🚀 JobHunter AI - Latest Jobs\n\n"

for _, job in df.iterrows():
    message += (
        f"🏢 {job['Company']}\n"
        f"💼 {job['Role']}\n"
        f"📍 {job['Location']}\n"
        f"🔗 {job['Link']}\n\n"
    )

response = requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    data={
        "chat_id": CHAT_ID,
        "text": message[:4000]
    }
)

print(response.status_code)
print(response.text)