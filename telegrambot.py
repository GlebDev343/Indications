import telebot
from telebot import types
import Indication
from Indication.models import Indication, MeteringDevice
from Indication.views import IndicationController

token = "6472590444:AAH911J01CgccTCDJ0Wbhb56desyqaqVH2Y"
bot = telebot.TeleBot(token)

markup2 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
indication_button = types.KeyboardButton('Indication')
markup2.add(indication_button)


@bot.message_handler(commands=['indication'])
def indication(message):
    bot.send_message(message.chat.id, "Enter current value:", reply_markup=markup2)
    msg = "Enter time of taking:\
           Example(2023-05-25 15:40)"
    bot.register_next_step_handler(msg, save_current_value)

def save_current_value(message):
    IndicationController.current_value = int(message.text)
    msg = "Enter number of  your metering device"
    bot.register_next_step_handler(msg, save_time_of_taking)

def save_time_of_taking(message):
    IndicationController.time_of_taking = message.text
    msg = "You have sent your indication successfully"
    bot.register_next_step_handler(msg, save_metering_device)

def save_metering_device(message):
    IndicationController.metering_device = int(message.text)
    IndicationController.post()

bot.polling(non_stop=True)