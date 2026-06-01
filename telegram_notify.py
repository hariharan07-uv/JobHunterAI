import pandas as pd
import requests
import os

BOT_TOKEN = os.environ["8957530045:AAGqnKMG7Y82SVWkVKlLSh0gWJLT1tvqLrI"]
CHAT_ID = os.environ["1850229207"]

df = pd.read_csv("all_jobs.csv")

message = "🚀 JobHunter AI - Latest Jobs\n\n"

for _, job in df.iterrows():
    message += (
        f"🏢 {job['Company']}\n"
        f"💼 {job['Role']}\n"
        f"📍 {job['Location']}\n"
        f"🔗 {job['Link']}\n\n"
    )

requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    data={
        "chat_id": CHAT_ID,
        "text": message[:4000]  # Telegram limit safety
    }
)

print("Telegram message sent")