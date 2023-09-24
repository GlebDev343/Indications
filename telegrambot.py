import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Indications.settings')

import django
django.setup()

import telebot
from telebot import types
from django.core.mail import send_mail
import Indication
from Indication.models import Indication, MeteringDevice, PersonalAccount
import Services
from Services.indication_service import save_value

token = "6472590444:AAH911J01CgccTCDJ0Wbhb56desyqaqVH2Y"
bot = telebot.TeleBot(token)

markup2 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
indication_button = types.KeyboardButton("Indication")
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
    try:
        global current_value
        current_value = int(message.text)
        bot.send_message(message.chat.id, "Enter your personal account number")
        bot.register_next_step_handler(message, save_account_number)
    except Exception:
        bot.send_message(message.chat.id, "Please enter a number:")
        bot.register_next_step_handler(message, save_current_value)

def save_account_number(message):
    try:
        global account_number
        account_number = int(message.text)
        personal_account = PersonalAccount.objects.get(account_number=account_number)
        send_mail(
            "Indication Bot",
            personal_account.verification_code,
            "IndicationBot@gmail.com",
            [personal_account.email]
        )
        bot.send_message(message.chat.id, "A confirmation code has been sent to your email address, enter it")
        bot.register_next_step_handler(message, check_and_save_record)
    except Exception as e:
        print(e)
        bot.send_message(message.chat.id, "Please enter a number:")
        bot.register_next_step_handler(message, save_account_number)

def check_and_save_record(message):
    try:
        PersonalAccount.objects.get(account_number=account_number, verification_code=message.text)
        save_value(cv=current_value, an=account_number)
        bot.send_message(message.chat.id, "Hurray!")
    except Exception:
        bot.send_message(message.chat.id, "Invalid verification code, try again:")
        bot.register_next_step_handler(message, check_and_save_record)
bot.infinity_polling()