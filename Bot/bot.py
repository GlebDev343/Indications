import telebot

token = "6472590444:AAH911J01CgccTCDJ0Wbhb56desyqaqVH2Y"
bot = telebot.TeleBot(token)

# registration_button = KeyboardButton('Registration', request_contact=True)
# keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(registration_button)

@bot.message_handler(commands=['start'])
def send_instructions(message):
	bot.send_message(message.chat.id, message, parse_mode="html")

@bot.message_handler()
def get_user_text(message):
	bot.send_message(message.chat.id, message, parse_mode="html")

bot.polling(non_stop=True)