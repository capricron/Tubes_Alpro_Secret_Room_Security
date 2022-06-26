from time import time
import telebot
from database import *
from function.loginFace import deteksiWajah
from function.closeDoor import closeDoor
from function.history import history
from function.registerFace import registerFace
from iot import closeGate
import time

bot = telebot.TeleBot('5425032096:AAExJldFOMQeuU5ef_u1O8K1Rdn_zuzDPvM')

@bot.message_handler(commands=['start', 'open', 'close', 'history', 'register'])
def main(message):
    mycursor.execute("SELECT status FROM door")
    door = mycursor.fetchone()
    password = "rahasia"
    args = message.text.split()
    match args[0]:
        case '/open':
            if door[0] == 1:
                bot.send_message(message.chat.id, 'Door is already open')   
            else:
                deteksiWajah(bot,message)           
        case '/close':
            if door[0] == 0:
                bot.send_message(message.chat.id, "Door is already closed")
            else:
                time.sleep(1)
                closeGate()
                closeDoor(bot,message)
        case '/history':
            history(bot,message)
        case '/register':
            registerFace(args,password,bot,message)
        case '/start':
            bot.send_message(message.chat.id, "Welcome to Door Bot")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()