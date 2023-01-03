from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ParseMode

from bot_loader import dp
from states.search import Search
import models


@dp.message_handler(commands='search')
async def search(message: types.Message):
    await Search.request.set()
    await message.reply("Введите запрос:")


# Сюда приходит ответ с запросом поиска
@dp.message_handler(state=Search.request)
async def process_search(message: types.Message, state: FSMContext):
    result = models.search(message.text)
    table = models.contacts_to_table(result)
    await message.reply(f'<pre>{table}</pre>', parse_mode=ParseMode.HTML)

    await state.finish()