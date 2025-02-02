import os
import requests
from dotenv import load_dotenv
from crawler import get_new_products


# Load environment variables from .env file
load_dotenv()

telegram_bot_token = os.environ.get('TELEGRAM_BOT_TOKEN')
# Validate token exists
if not telegram_bot_token:
    raise ValueError("Telegram bot token not found! Please check your .env file.")

def send_message(message):
    response = requests.post(
            url=f'https://api.telegram.org/bot{telegram_bot_token}/sendMessage',
            data={'chat_id': -4699774455, 'text': message}
        ).json()
    return response



if __name__ == "__main__":
    message = get_new_products()
    send_message(message)