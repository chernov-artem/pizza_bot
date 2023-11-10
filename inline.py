from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token="5864201176:AAF6PuhZLBJBAlK1SPH4jn3dFBbUnlEPh-I")
dp = Dispatcher(bot)

# Кнопка-ссылка

urlkb = InlineKeyboardMarkup(row_width=1)
urlButton = InlineKeyboardButton(text="Ссылка", url="youtube.com")
urlButton2 = InlineKeyboardButton(text="Ссылка2", url="google.com")
x = [InlineKeyboardButton(text="Ссылка3", url="youtube.com"),
     InlineKeyboardButton(text="Ссылка4", url="google.com"),
     InlineKeyboardButton(text="Ссылка5", url="google.com")]
urlkb.add(urlButton, urlButton2).row(*x)

@dp.message_handler(commands='ссылки')
async def url_comand(message: types.Message):
        await message.answer('Ссылочки', reply_markup=urlkb)

executor.start_polling(dp, skip_updates=True)
