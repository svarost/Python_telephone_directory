from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from bot_config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Для просмотра ")

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отправлю этот текст тебе в ответ!")

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)

@dp.message_handler(commands=['Добавить контакт'])
async def process_add_contact_command(message: types.Message):
    await message.reply("Введите фамилию")



if __name__ == '__main__':
    executor.start_polling(dp)