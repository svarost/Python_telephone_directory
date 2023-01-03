from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
import aiogram.utils.markdown as md
from aiogram.types import ParseMode

from bot_loader import dp, bot
from states.input import InputContactForm
import models



@dp.message_handler(Command('input_contact'), state=None)
async def input_contact(message: types.Message):
    await InputContactForm.last_name.set()
    await message.reply("Введите фамилию контакта:")


# Добавляем возможность отмены, если пользователь передумал заполнять
@dp.message_handler(state='*', commands='cancel')
@dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return

    await state.finish()
    await message.reply('ОК')


# Сюда приходит ответ с фамилией
@dp.message_handler(state=InputContactForm.last_name)
async def process_last_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['last_name'] = message.text

    await InputContactForm.next()
    await message.reply("Введите имя контакта:")


# Сюда приходит ответ с именем
@dp.message_handler(state=InputContactForm.name)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

    await InputContactForm.next()
    await message.reply("Введите номер телефона контакта:")


# Сюда приходит ответ с номером телефона
@dp.message_handler(state=InputContactForm.tel_number)
async def process_tel_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['tel_number'] = message.text

    await InputContactForm.next()
    await message.reply("Введите номер категорию контакта:")


# Сюда приходит ответ с категорией контакта
@dp.message_handler(state=InputContactForm.notion)
async def process_notion(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['notion'] = message.text
        markup = types.ReplyKeyboardRemove()
        print(data.values())
        models.dictionary_w(data.values())

        await bot.send_message(
            message.chat.id,
            md.text(
                md.text('Контакт'),
                md.text('Фамилия:', data['last_name']),
                md.text('Имя:', data['name']),
                md.text('Номер телефона:', data['tel_number']),
                md.text('Категория:', data['notion']),
                sep='\n',
            ),
            reply_markup=markup,
            parse_mode=ParseMode.MARKDOWN,
        )

    await state.finish()