from aiogram.types import  BotCommand 




private = [
    BotCommand(command='menu', description='Посмотреть меню'),
    BotCommand(command='about', description='О нас'),
    BotCommand(command='payment', description='Варианты оплаты'),
    BotCommand(command='shipping', description='Варианты доставки'),
]   # меню - это список команд, которые будут отображаться в меню бота