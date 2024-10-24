import telebot
import ccxt
import config

# Inicializa el bot de Telegram solo con el token
bot = telebot.TeleBot(config.TELEGRAM_TOKEN)

# Inicializa la conexión con Bitget usando API_KEY, SECRET_KEY y PASSWORD
ex = ccxt.bitget({
    'apiKey': config.API_KEY,
    'secret': config.SECRET_KEY,
    'password': config.PASSWORD,
    'enableRateLimit': True
})


def obtener_balance_futuros():
    positions = ex.fetch_positions()
    return positions

# Función para manejar los comandos /start y /help


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    resultados = obtener_balance_futuros()

    # Construir el mensaje para todas las posiciones
    respuesta = ""
    for posicion in resultados:
        respuesta += f"Symbol: {posicion.get('symbol')}\nSide: {posicion.get('side')}\nCantidad: {posicion.get('contracts')}\nPnl: {posicion.get('unrealizedPnl')}\n"

    # Enviar el mensaje completo al usuario de Telegram
    bot.reply_to(message, respuesta)


# Iniciar la escucha del bot
bot.infinity_polling()
