import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Indications.settings')

import django
django.setup()

import telebot
from telebot import types
import Indication
from Indication.models import Indication, MeteringDevice
import Services
from Services.indication_service import save_value

token = "6472590444:AAH911J01CgccTCDJ0Wbhb56desyqaqVH2Y"
bot = telebot.TeleBot(token)

markup2 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
indication_button = types.KeyboardButton('Indication')
markup2.add(indication_button)

@bot.message_handler(commands=['start'])
def indication(message):
    bot.send_message(message.chat.id, "Hello", reply_markup=markup2)
    bot.register_next_step_handler(message, indication)

@bot.message_handler(commands=['indication'])
def indication(message):
    bot.send_message(message.chat.id, "Enter current value:")
    bot.register_next_step_handler(message, save_current_value)

def save_current_value(message):
    global current_value
    current_value = int(message.text)
    bot.send_message(message.chat.id, "Enter your personal account number")
    bot.register_next_step_handler(message, save_account_number)

def save_account_number(message):
    account_number = int(message.text)
    save_value(cv=current_value, an=account_number)
    bot.send_message(message.chat.id, "Hurray!")

bot.infinity_polling()