from aiogram import Dispatcher, types, Bot
from aiogram.filters import CommandStart
from asyncio import run
from function import *
from config import *


dp = Dispatcher()

async def startAnswer(bot: Bot):
    await bot.send_message(chat_id=admin_id, text='Bot ishladi ✅')

async def shutdownAnswer(bot: Bot):
    await bot.send_message(chat_id=admin_id, text='Bot ishdan toxtadi ❌')


async def start():
    dp.startup.register(startAnswer)
    dp.message.register(startCommandAnswer, CommandStart())
    dp.message.register(userInputMessage)
    dp.shutdown.register(shutdownAnswer)



    bot = Bot(token=token)
    await dp.start_polling(bot, polling_timeout=1)

run(start())