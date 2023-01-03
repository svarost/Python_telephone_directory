from aiogram import types
from aiogram.dispatcher import FSMContext

from bot_loader import dp
from states.export_to_csv import Export_csv
import models


@dp.message_handler(commands='export_csv')
async def export_csv(message: types.Message, state: FSMContext):
    await Export_csv.export_csv.set()
    await message.reply('Для экспорта в кодировки MS Excell, напишите '
         '"Excel", иначе напишите любоее сообщение.')

@dp.message_handler(state=Export_csv.export_csv)
async def process_export_csv(message: types.Message, state: FSMContext):
    if message.text.lower() == 'excel':
        models.export_to_csv('Excel')
    else:
        models.export_to_csv()
    await message.reply_document(open('Dictionary.csv', 'rb'))

    await state.finish()