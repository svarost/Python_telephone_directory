import logging

from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
import aiogram.utils.markdown as md
from aiogram.types import ParseMode
from bot_config import TOKEN
from bot_utils import TestStates
from bot_messages import MESSAGES

import models


logging.basicConfig(format=u'%(filename)+13s [ LINE:%(lineno)-4s] %(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.DEBUG)


bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
storege = MemoryStorage()

dp.middleware.setup(LoggingMiddleware())


# создаём форму и указываем поля
class Form(StatesGroup):
    last_name = State()
    name = State()
    tel_number = State()
    notion = State()

class Search(StatesGroup):
    request = State()


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


@dp.message_handler(commands=['input_contact'])
async def input_contact(message: types.Message):
    await Form.last_name.set()
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
@dp.message_handler(state=Form.last_name)
async def process_last_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['last_name'] = message.text

    await Form.next()
    await message.reply("Введите имя контакта:")


# Сюда приходит ответ с именем
@dp.message_handler(state=Form.name)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

    await Form.next()
    await message.reply("Введите номер телефона контакта:")


# Сюда приходит ответ с номером телефона
@dp.message_handler(state=Form.tel_number)
async def process_tel_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['tel_number'] = message.text

    await Form.next()
    await message.reply("Введите номер категорию контакта:")


# Сюда приходит ответ с категорией контакта
@dp.message_handler(state=Form.notion)
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


@dp.message_handler(commands='search')
async def input_contact(message: types.Message):
    await Search.request.set()
    await message.reply("Введите запрос:")


# Сюда приходит ответ с запросом поиска
@dp.message_handler(state=Search.request)
async def process_notion(message: types.Message, state: FSMContext):
    print(message.text)
    result = models.search(message.text)
    table = models.contacts_to_table(result)
    await message.reply(f'<pre>{table}</pre>', parse_mode=ParseMode.HTML)

    await state.finish()


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


if __name__ == '__main__':
    executor.start_polling(dp, on_shutdown=shutdown)