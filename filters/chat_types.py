from aiogram.filters import Filter 
from aiogram import types
from typing import List




class ChatTypeFilter(Filter):                         
    # создаем класс ChatTypeFilter, который наследуется от Filter
    def __init__(self, chat_types: List[str]) -> None:
        self.chat_types = chat_types 

    async def __call__(self, message: types.Message) -> bool:
        return message.chat.type in self.chat_types