@echo off

call %~dp0 telegram_bot\venv\Scripts\activate

cd %~dp0 telegram_bot

set TOKEN = 5864201176:AAF6PuhZLBJBAlK1SPH4jn3dFBbUnlEPh-I

python telegram_bot.py

pause