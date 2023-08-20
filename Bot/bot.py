from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types.contact import Contact

bot = Bot("6472590444:AAH911J01CgccTCDJ0Wbhb56desyqaqVH2Y")
dp = Dispatcher(bot)

registration_button = KeyboardButton('Registration', request_contact=True)
keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(registration_button)

@dp.message_handler(commands=['start'])
async def send_instructions(message: types.Message):
	await message.answer("In order to give meter readings, enter the command: /indication", reply_markup=keyboard)

@dp.message_handler()
async def send(message: types.Message, state: FSMContext):
	await state.finish()
	await message.answer(message.contact.phone_number)
	print(message)

executor.start_polling(dp)