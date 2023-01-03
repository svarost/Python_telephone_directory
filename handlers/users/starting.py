from aiogram import types
from aiogram.types import ParseMode

from bot_loader import dp, bot
from bot_messages import MESSAGES
import models



@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(MESSAGES['start'])


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(MESSAGES['help'])


@dp.message_handler(commands=['view_contacts'])
async def process_help_command(message: types.Message):
    table = models.contacts_to_table(models.dictionary_r())
    await message.reply(f'<pre>{table}</pre>', parse_mode=ParseMode.HTML)


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)