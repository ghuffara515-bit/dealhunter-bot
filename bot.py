import telebot
import requests
import os

TOKEN = os.environ.get("TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 
        "🎉 Welcome to DealHunter PK! 🎉\n\n"
        "💥 Pakistan ka #1 AliExpress Deals Bot!\n\n"
        "🛍️ Hum aapke liye rozana\n"
        "   dhoondh ke laate hain:\n\n"
        "   ✅ Sasti se sasti deals\n"
        "   ✅ Top quality products\n"
        "   ✅ Trusted AliExpress links\n"
        "   ✅ Daily updated offers\n\n"
        "💰 Paisa bachao — Smart shopping karo!\n\n"
        "━━━━━━━━━━━━━━━━━\n"
        "📌 Commands:\n"
        "🔥 /deals - Aaj ki hot deals\n"
        "❓ /help  - Madad chahiye?\n"
        "━━━━━━━━━━━━━━━━━\n\n"
        "👇 Abhi /deals type karo\n"
        "aur deals dekho! 🚀"
    )

@bot.message_handler(commands=['deals'])
def send_deals(message):
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
