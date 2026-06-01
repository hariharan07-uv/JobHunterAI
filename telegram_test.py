import requests

BOT_TOKEN = "8957530045:AAGqnKMG7Y82SVWkVKlLSh0gWJLT1tvqLrI"
CHAT_ID = "1850229207"

message = """
🚀 JobHunter AI Test

If you received this message,
Telegram integration is working!
"""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

response = requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": message
    }
)

print(response.status_code)
print(response.text)