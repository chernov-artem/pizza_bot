from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
import os

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token="5864201176:AAF6PuhZLBJBAlK1SPH4jn3dFBbUnlEPh-I")
dp = Dispatcher(bot)

answ = dict()

# Кнопка-ссылка

urlkb = InlineKeyboardMarkup(row_width=2)
urlButton = InlineKeyboardButton(text="Ссылка", url="youtube.com")
urlButton2 = InlineKeyboardButton(text="Ссылка2", url="google.com")
x = [InlineKeyboardButton(text="Ссылка3", url="youtube.com"),
     InlineKeyboardButton(text="Ссылка4", url="google.com"),
     InlineKeyboardButton(text="Ссылка5", url="google.com")]
urlkb.add(urlButton, urlButton2).row(*x)

@dp.message_handler(commands='ссылки')
async def url_comand(message: types.Message):
        await message.answer('Ссылочки', reply_markup=urlkb)

inkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='лайк', callback_data='like_1'),
                                             InlineKeyboardButton(text='Не лайк', callback_data='like_-1'))

@dp.message_handler(commands='test')
async def test_command(message: types.Message):
    await message.answer('За видео про деплой бота', reply_markup=inkb)

@dp.callback_query_handler(Text(startswith='like_'))
async def www_call(callback: types.callback_query):
    res = int(callback.data.split('_')[1])
    if f"{callback.from_user.id}" not in answ:
        answ[f"{callback.from_user.id}"] = res
        await callback.answer('Вы проголосовали')
    else:
        await callback.answer("Вы уже проголосовали", show_alert=True)

    await callback.answer('Нажата инлайн кнопка')
    await callback.answer()

executor.start_polling(dp, skip_updates=True)
