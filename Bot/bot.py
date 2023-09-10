import sys

import telebot
from telebot import types
import Indication
from .models import Indication, InstalledMeteringDevice, MeteringDevice, Manufacturer, PersonalAccount, MeterModel

token = "6472590444:AAH911J01CgccTCDJ0Wbhb56desyqaqVH2Y"
bot = telebot.TeleBot(token)

markup1 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
register_button = types.KeyboardButton('Register personal account')
markup1.add(register_button)


@bot.message_handler(commands=['start'])
def send_instructions(message):
	bot.send_message(message.chat.id, "Please, register your personal account:", reply_markup=markup1)
	msg = "Enter your personal account number:"
	bot.register_next_step_handler(msg, bound_personal_account)

def bound_personal_account(message):
	global account_number
	account_number = message.text
	msg = "Enter your first name:"
	bot.register_next_step_handler(msg, save_first_name)

def save_first_name(message):
	global first_name
	first_name = message.text
	msg = "Enter your last name:"
	bot.register_next_step_handler(msg, save_last_name)

def save_last_name(message):
	global last_name
	last_name = message.text
	msg = "Enter your patronymic:"
	bot.register_next_step_handler(msg, save_patronymic)

def save_patronymic(message):
	global patronymic
	patronymic = message.text
	msg = "Enter your address:"
	bot.register_next_step_handler(msg, save_address)

def save_address(message):
	global address
	address = message.text
	msg = "Enter your phone number:"
	bot.register_next_step_handler(msg, save_phone_number)

def save_phone_number(message):
	global phone_number
	phone_number = int(message.text)
	msg = "Enter your email address:"
	bot.register_next_step_handler(msg, save_email)

meter_models = [i.model_name for i in MeterModel.objects.all()]
markup3 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
for i in meter_models:
	markup3.add(i)

def save_email(message):
	global email
	email = message.text
	bot.reply_to(message, "Congratulations! You have registered your account!\
                           Now you can bound your metering device")
	bot.send_message(message.chat.id, "Please, select your model of metering device", reply_markup=markup3)
	bot.register_next_step_handler(msg, select_meter_model)

	q1 = PersonalAccount.objects.create(first_name=first_name,
										last_name=last_name,
										patronymic=patronymic,
										address=address,
										account_number=account_number,
										phone_number=phone_number,
										email=email)
	q1.save()

def select_meter_model(message):
	global model_metering_device
	model_metering_device = message.text
	msg = "Enter number of your metering device:"
	bot.register_next_step_handler(msg, save_number_of_metering_device)

def save_number_of_metering_device(message):
	global number_of_metering_device
	number_of_metering_device = int(message.text)
	msg = "Enter installation date of your metering device:\
		   Example(2000-05-25)"
	bot.register_next_step_handler(msg, save_installation_date)

def save_installation_date(message):
	global installation_date
	installation_date = message.text
	msg = "Enter date of issue your metering device:\
	       Example(2000-05-25)"
	bot.register_next_step_handler(msg, save_date_of_issue)

def save_date_of_issue(message):
	global date_of_issue
	date_of_issue = message.text
	bot.reply_to(message, "Congratulations! You have bounded your metering device. Now you can give indications")
	
	q2 = MeteringDevice.objects.create(number=number_of_metering_device,
                                   model_metering_device=MeterModel.objects.find(model_name=model_metering_device),
							       date_of_issue=date_of_issue)
    q2.save()

	q3 = InstalledMeteringDevice.objects.create(personal_account=PersonalAccount.objects.find(account_number=account_number),
    	                                        metering_device=MeteringDevice.objects.find(number=number_of_metering_device,
										                                                    model_metering_device=model_metering_device),
										        installation_date=installation_date)
	q3.save()

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
	global current_value
	current_value = int(message.text)
	msg = "Enter number of  your metering device"
	bot.register_next_step_handler(msg, save_time_of_taking)

def save_time_of_taking(message):
	global time_of_taking
	time_of_taking = message.text
	msg = "You have sent your indication successfully"
	bot.register_next_step_handler(msg, save_metering_device)

def save_metering_device(message):
	global metering_device
	metering_device = message.text
    q4 = Indication.objects.create(current_value=current_value,
                          	   time_of_taking=time_of_taking,
						  	   metering_device=MeteringDevice.objects.find(number=metering_device))
    q4.save()

bot.polling(non_stop=True)