from string import punctuation

from aiogram import F, types, Router 
from aiogram.filters import CommandStart, Command, or_f 
from filters.chat_types import ChatTypeFilter


user_group_router = Router()                                                            
# создаем роутер                                      
user_group_router.message.filter(ChatTypeFilter(['group', 'supergroup']))               
# фильтруем сообщения по типу чата (private, group, supergroup)

restricted_words = {'кабан', 'хомяк', 'выхухоль'}                                       
# создаем множество запрещенных слов






def clean_text(text: str) -> str:
    return text.translate(str.maketrans('', '', punctuation))


@user_group_router.edited_message()                                                    
 # реагирует на отредактированное сообщение
@user_group_router.message()
async def cleaner(message: types.Message):
    if restricted_words.intersection(clean_text(message.text.lower()).split()):
        await message.answer(f"{message.from_user.first_name}, соблюддайте порядок в чате!")
        await message.delete()                                                          
        # удаляем сообщение, если в нем есть запрещенные слова
        # await message.chat.ban(message.from_user.id)                                  
        # баним пользователя

