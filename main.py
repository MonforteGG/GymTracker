from dotenv import load_dotenv

from bot import bot

# Cargar las variables de entorno del archivo .env
load_dotenv()


bot.polling()

