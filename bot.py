import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from db_operations import guardar_usuario



# Inicializar el bot de Telegram
bot = telebot.TeleBot(os.getenv('TELEGRAM_TOKEN'))

# Variables globales
username = ""
password = ""
entreno_findes = False
chat_id = ""

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Bienvenido a GymTracker! Escribe /register si aún no tienes una cuenta.")


@bot.message_handler(commands=['register'])
def send_register_message(message):
    bot.reply_to(message, "Vamos a proceder a registrarte.")
    bot.send_message(message.chat.id, "Introduce tu nombre de usuario:")
    bot.register_next_step_handler(message, get_username)


def get_username(message):
    global username  # Declarar la variable como global
    username = message.text
    print(f"Nombre de usuario recibido: {username}")
    bot.send_message(message.chat.id, "Introduce tu contraseña:")
    bot.register_next_step_handler(message, get_password)


def get_password(message):
    global password  # Declarar la variable como global
    password = message.text
    print(f"Contraseña recibida: {password}")

    # Crear botones para la pregunta sobre entrenar los fines de semana
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("Sí 🏋️‍♂️", callback_data='entrenar_si'),
        InlineKeyboardButton("No ❌", callback_data='entrenar_no')
    )

    bot.send_message(message.chat.id, "¿Vas a entrenar los fines de semana?", reply_markup=markup)


# Manejar la respuesta del botón de entrenamiento fines de semana
@bot.callback_query_handler(func=lambda call: call.data.startswith('entrenar_'))
def handle_entreno_findes(call):
    global entreno_findes  # Declarar la variable como global
    entreno_findes = (call.data.split('_')[1] == "si")  # True o False según la respuesta
    print(f"Entreno fines de semana recibido: {entreno_findes}")

    # Crear botones para seleccionar días de entrenamiento
    markup = InlineKeyboardMarkup()

    if entreno_findes:
        # Botones del 1 al 7
        dias = [str(i) for i in range(1, 8)]
    else:
        # Botones del 1 al 5
        dias = [str(i) for i in range(1, 6)]

    for dia in dias:
        markup.add(InlineKeyboardButton(dia, callback_data=f'dia_{dia}'))

    bot.send_message(call.message.chat.id, "Selecciona cuántos días vas a entrenar a la semana:", reply_markup=markup)


# Manejar la respuesta del botón de días de entrenamiento
@bot.callback_query_handler(func=lambda call: call.data.startswith('dia_'))
def handle_dias_entrenamiento(call):
    dias_entreno_por_semana = call.data.split('_')[1]  # Obtener el día seleccionado
    print(f"Días de entreno seleccionados: {dias_entreno_por_semana}")

    bot.send_message(call.message.chat.id, "¡Registro completo!")

    # Aquí puedes guardar los datos en tu base de datos
    guardar_usuario(username, password, entreno_findes, dias_entreno_por_semana, call.message.chat.id)


# Iniciar el bot
bot.polling()
