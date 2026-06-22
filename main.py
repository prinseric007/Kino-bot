import os
from flask import Flask
from threading import Thread
import telebot

# 1. Токен ва Ботни созлаш
BOT_TOKEN = "8382890125:AAHgdLV4ubYwPOxSQ3fUwt5tHuX-90hggzE"  # Бу ерга BotFather берган токенни ёзинг
bot = telebot.TeleBot(BOT_TOKEN)

app = Flask('')

@app.route('/')
def home():
    return "Бот фаол ишлаяпти!"

def run():
    app.run(host='0.0.0.0', port=8080)

# 2. БОТ БУЙРУҚЛАРИ (Кино кодлари шу ерда)

# /start буйруғи берилганда
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(
        message.chat.id, 
        "👋 **Салом! Кино ботга хуш келибсиз!**\n\n🍿 Кино кўриш учун кино кодини юборинг."
    )

# Кино кодларини текшириш қисми
@bot.message_handler(func=lambda message: True)
def send_movie(message):
    kod = message.text

    # 1-КИНО (Масалан, код: 100)
    if kod == "101":
        bot.send_video(
            message.chat.id, 
            "BAACAgQAAxkBAAFM1NlqNIYtOTA5ni4odP-SRalqJGVhvwACFRsAAssmgVCoG1HjVkt_-DwE",  # Бу ерга биринчи кинонинг файл идисини қўясиз
            caption="🎬 **Кино номи:** Синфдош\n\n🍿 Ёқимли томоша!"
        )

    elif kod == "102":
        bot.send_video(
            message.chat.id, 
            "BAACAgQAAxkBAAFM1xNqNMDX3WKph56cRkCunZVSnhmUfgACzBkAAv96gFBOFBsc3lKVzTwE",  # Бу ерга иккинчи кинонинг файл идисини қўясиз
            caption="🎬 **Кино номи:** Якин масофа\n\n🍿 Ёқимли томоша!"
        )

    elif kod == "103":
        bot.send_video(
            message.chat.id, 
            "BAACAgIAAxkBAAFM1PVqNIfoR-m4YALqeUKGuxtm0t3vaAACNoIAAiEMAAFIO6Xr-2U2ehI8BA", 
            caption="🎬 **Номи:** Гриландия 1\n\n🍿Ёкимли томоша!"
        )

        bot.send_video(
            message.chat.id,
            "BAACAgUAAxkBAAFM1MlqNIVCYxkwHVCUn7vWmEyvYRiiewAC8SAAAivxcFftRiVP_0_s6zwE",
            caption="🎬 **номи:** Гриландия 2\n\n🍿Ёкимли томоша!"
        )

    elif kod == "104":
        bot.send_video(message.chat.id, "BAACAgIAAxkBAAFNGNtqONMzMrOvsCLG_vC-KBxKudXRuAACQ4YAApcQuUi_f3nQRrsNOTwE", caption="🎬 **Номи:** Танк\n\n🍿Ёкимли томоша!")

    # Янги кино қўшмоқчи бўлсангиз, мана шу пастдаги блокни нусхалаб кўпайтираверасиз:
    # elif kod == "ЯНГИ_КОД":
    #     bot.send_video(message.chat.id, "ЯНГИ_ФАЙЛ_ИД", caption="🎬 **Номи:** ...\n\n🗓 **Йили:** ...")

    else:
        bot.send_message(
            message.chat.id, 
            "❌ **Бундай кодли кино топилмади.**\n\nИлтимос, кодни тўғри ёзганингизни текшириб кўринг."
        )

# Ботни серверда юргизиш
def keep_alive():
    t = Thread(target=run)
    t.start()

if __name__ == "__main__":
    keep_alive()
    print("Бот ишга тушди...")
    bot.infinity_polling()
    
