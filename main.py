from numpy import percentile
import telebot
from loginFace import deteksiWajah
from closeDoor import closeDoor
from database import mycursor
from history import history
from registerFace import registerFace

bot = telebot.TeleBot('5425032096:AAExJldFOMQeuU5ef_u1O8K1Rdn_zuzDPvM')

@bot.message_handler(commands=['start', 'help', 'open', 'close', 'history', 'register'])
def main(message):
    door = 0
    mycursor.execute("SELECT status FROM door")
    door = mycursor.fetchone()
    args = message.text.split()

    match args[0]:
        case '/open':
            if door[0] == 1:
                bot.send_message(message.chat.id, "Door is already open")
            else:
                deteksiWajah(bot,message)
        case '/close':
            if door[0] == 0:
                bot.send_message(message.chat.id, "Door is already closed")
            else:
                closeDoor(bot,message)
        case '/history':
            history(bot,message)
        case '/register':
            registerFace(args,bot,message)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()