from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ParseMode

from bot_loader import dp
from states.delete import Delete_contact
import models


@dp.message_handler(commands='delete')
async def delete(message: types.Message, state: FSMContext):
    await Delete_contact.delete.set()
    table = models.contacts_to_table(models.dictionary_r())
    await message.reply(f'<pre>{table}</pre>', parse_mode=ParseMode.HTML)
    await message.reply("Укажите порядковый номер контакта, который необходимо удалить:")


# Сюда приходит ответ с номером контакта для удаления
@dp.message_handler(state=Delete_contact.delete)
async def process_delete(message: types.Message, state: FSMContext):
    models.delete(int(message.text))
    table = models.contacts_to_table(models.dictionary_r())
    await message.reply(f'<pre>{table}</pre>', parse_mode=ParseMode.HTML)

    await state.finish()
