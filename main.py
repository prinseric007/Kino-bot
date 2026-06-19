import telebot
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

# 1. Сервер учун керакли кичик тизим (ухлаб қолмаслик учун)
class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Bot is alive!")

def run_health_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(('0.0.0.0', port), HealthCheckHandler)
    server.serve_forever()

# --- СИЗНИНГ БОТИНГИЗ КИСМИ ---
API_TOKEN = '8382890125:AAHgdLV4ubYwPOxSQ3fUwt5tHuX-90hggzE' 
bot = telebot.TeleBot(API_TOKEN)

KINO_BAZA = {
    "101": "BAACAgQAAxkBAAFM1NlqNIYtOTA5ni4odP-SRalqJGVhvwACFRsAAssmgVCoG1HjVkt_-DwE",
}

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Салом! Кино кодини юборинг 🎬")

@bot.message_handler(func=lambda message: True)
def get_movie(message):
    kod = message.text
    if kod in KINO_BAZA:
        bot.send_video(message.chat.id, KINO_BAZA[kod], caption="🎬**Синфдош**\n\n Код: {kod}")
    else:
        bot.reply_to(message, "Бундай кодли кино топилмади 😔")

# 2. Серверни алоҳида оқимда юргизиш
threading.Thread(target=run_health_server, daemon=True).start()

print("Бот сервер учун тайёр...")
bot.polling(none_stop=True)
