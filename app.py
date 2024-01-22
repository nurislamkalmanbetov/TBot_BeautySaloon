import asyncio
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import BotCommandScopeAllPrivateChats

from dotenv import find_dotenv, load_dotenv                                             # pip install python-dotenv
load_dotenv(find_dotenv())                                                              # загружаем переменные окружения из файла .env

from handlers.user_private import user_private_router                                   # импортируем роутер из файла handlers/user_private.py
from handlers.user_group import user_group_router                                       # импортируем роутер из файла handlers/user_group.py
from common.bot_cmds_list import private                                                # импортируем список команд для бота


ALLOWED_UPDATES = ['message, edited_message']                                           
# разрешаем обновления только для сообщений и отредактированных сообщений

bot = Bot(token=os.getenv('TOKEN'))                                                     # хранится в файле .env
dp = Dispatcher()                                                                       # создаем диспетчер



dp.include_router(user_private_router)                                                  # user_private_router - это переменная, которая содержит в себе все хэндлеры из файла handlers/user_private.py
dp.include_router(user_group_router)                                                    # user_group_router - это переменная, которая содержит в себе все хэндлеры из файла handlers/user_group.py




async def main() -> None:
    await bot.delete_webhook(drop_pending_updates=True)                                 # удаляем вебхук, если он был установлен
    await bot.set_my_commands(commands=private, scope=BotCommandScopeAllPrivateChats()) # удаляем все команды у бота + добавляем новые в меню
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)                        # запускаем лонг поллинг


asyncio.run(main())                                                                     # запускаем асинхронную функцию main()

