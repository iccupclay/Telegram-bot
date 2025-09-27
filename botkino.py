from telebot import TeleBot, types

bot = TeleBot("7959291954:AAFxchyteSx9WxUqReKfnL1WURgqpNLuynY")  # Tokenni yashiring!

# 🎬 Kinolar bazasi
films = {
    "1": "https://t.me/shokh_movie/21",
    "2": "https://t.me/shokh_movie/22",
    "3": "https://t.me/shokh_movie/23",
}

# /start komandasi
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    kanal_btn = types.InlineKeyboardButton("📢 Telegram Kanal", url="https://t.me/shokh_movie")
    insta_btn = types.InlineKeyboardButton("📸 Instagram", url="https://www.instagram.com/shokh_movie?igsh=MXI3bnR6MTNvZHZ6Yg==")
    markup.add(kanal_btn, insta_btn)

    text = (
        "Assalomu alaykum! 🎬\n"
        "Botimizga xush kelibsiz!\n\n"
        "👉 Qidirayotgan kino kodini yozib yuboring.\n"
        "Masalan: 1, 2, 3"
    )

    bot.send_message(message.chat.id, text, reply_markup=markup, parse_mode="Markdown")

# 🔍 Kino qidirish
@bot.message_handler(func=lambda message: True)
def search(message):
    query = message.text.strip()

    if query in films:
        bot.send_message(message.chat.id, f"🎬 Mana siz izlagan kino:\n{films[query]}")
    else:
        bot.send_message(message.chat.id, "😔 Bunday kod topilmadi. Iltimos, boshqa kod yozib ko‘ring.")

bot.polling()