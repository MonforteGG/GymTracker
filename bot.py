import os
import telebot
from dotenv import load_dotenv

# Cargar las variables de entorno del archivo .env
load_dotenv()


# Inicializar el bot de Telegram
bot = telebot.TeleBot(os.getenv('TELEGRAM_TOKEN'))


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Estoy funcionando correctamente!")



# Iniciar el bot
bot.polling()