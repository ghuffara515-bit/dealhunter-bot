import telebot
import requests
import os

# Telegram Bot Token
TOKEN = "8657762610:AAEPhVPlejvZLE2M5FAD1ps14dUoCROLD3o"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the AliExpress Deals Bot! Type /deals to see current offers.")

@bot.message_handler(commands=['deals'])
def send_deals(message):
    # This is a placeholder for actual AliExpress API integration.
    # In a real scenario, you'd fetch these from an API.
    deals_text = (
        "🔥 *Today's Top AliExpress Deals* 🔥\n\n"
        "1. Wireless Bluetooth Earbuds - $5.99\n"
        "🔗 [View Deal](https://www.aliexpress.com)\n\n"
        "2. Smart Watch Series 7 Clone - $12.45\n"
        "🔗 [View Deal](https://www.aliexpress.com)\n\n"
        "3. Portable Power Bank 10000mAh - $8.90\n"
        "🔗 [View Deal](https://www.aliexpress.com)\n\n"
        "Use /deals anytime to refresh!"
    )
    bot.send_message(message.chat.id, deals_text, parse_mode='Markdown')

if __name__ == "__main__":
    print("Bot is starting...")
    bot.infinity_polling()
