from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token="5864201176:AAF6PuhZLBJBAlK1SPH4jn3dFBbUnlEPh-I")
dp = Dispatcher(bot, storage=storage)