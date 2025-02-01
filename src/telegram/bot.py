import os
import telebot

telegram_bot_token = os.get_env('TELEGRAM_BOT_TOKEN')

bot = telebot.TeleBot(telegram_bot_token)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hi, what do you need today?")
