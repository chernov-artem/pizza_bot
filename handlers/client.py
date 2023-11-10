from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.types import ReplyKeyboardRemove
from keyboards import kb_client
from data_base import sqlite_db

# @dp.message_handler(commands=['start', 'help'])
async def commands_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита!', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply("Общение с ботов в ЛС. Напишите ему http://t.me/spb97192568_test_pizza_bot")

# @dp.message_handler(commands=['Режим_работы'])
async def pizza_open_command(messgage : types.Message):
    await bot.send_message(messgage.from_user.id, "Время работы с 10:00 до 23:00")
    await messgage.delete()

# @dp.message_handler(commands=['Расположение'])
async def pizza_place_command(message : types.Message):
    await bot.send_message(message.from_user.id, "мы находимся в Хуево-Кукуево д.5", reply_markup=ReplyKeyboardRemove())

async def pizza_menu_command(message: types.Message):
    await sqlite_db.sql_read(message)

def register_handlers_client(dp : Dispatcher):

    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands=['Режим_работы'])
    dp.register_message_handler(pizza_place_command, commands=['Расположение'])
    dp.register_message_handler(pizza_menu_command, commands=['Меню'])