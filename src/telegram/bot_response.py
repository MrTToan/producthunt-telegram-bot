import os
from dotenv import load_dotenv
import telebot

# Load environment variables from .env file
load_dotenv()

telegram_bot_token = os.environ.get('TELEGRAM_BOT_TOKEN')
# Validate token exists
if not telegram_bot_token:
    raise ValueError("Telegram bot token not found! Please check your .env file.")

bot = telebot.TeleBot(telegram_bot_token)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hi, what do you need today?")


# if __name__ == "__main__":
#     print("Bot is running...")
#     bot.polling()