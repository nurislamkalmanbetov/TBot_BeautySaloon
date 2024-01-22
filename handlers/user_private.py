from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command, or_f
from filters.chat_types import ChatTypeFilter



user_private_router = Router()                                                              
# создаем роутер
user_private_router.message.filter(ChatTypeFilter(['private']))                    
# фильтруем сообщения по типу чата в личку (private)





@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message) -> None:
    await message.answer('Привет, я виртуальный помощник')


# @user_private_router.message(F.text.lower() == "меню")
@user_private_router.message(or_f(Command("menu"), (F.text.lower() == "меню")))
async def menu_cmd(message: types.Message):
    await message.answer('Вот меню: ')


@user_private_router.message(F.text.lower() == "о нас") 
# реагирует на текст "о нас" и "about"
@user_private_router.message(Command('about'))
async def about_cmd(message: types.Message):
    await message.answer("О нас:")


@user_private_router.message((F.text.lower() == 'варианты оплаты'))
@user_private_router.message(Command('payment'))
async def pament_cmd(message: types.Message):
    await message.answer("Варианты оплаты:")


@user_private_router.message((F.text.lower().contains('доставк')) | (F.text.lower() == 'варианты доставки'))
@user_private_router.message(Command('shipping'))
async def menu_cmd(message: types.Message):
    await message.answer("Варианты доставки:")  
    # реагирует на текст "доставк" и "варианты доставки - отправляет сообщение "Это магический фильтр"