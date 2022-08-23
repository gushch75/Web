from aiogram.utils import executor
from aiogram import types
import json
from aiogram import Bot,Dispatcher,types
global users
API= '5410393603:AAGrC8faoNm6E3F4H_FfIcllPuVRW3w_aDU'
contacts_file = 'contacts copy.json'

bot = Bot(token=API)
dp = Dispatcher(bot)
#__all__ = ['dp']
__all__ = ['dp','contacts_file','users']

users = {}
contact_book_admins = {}



@dp.message_handler(text="Safe")
@dp.message_handler(commands=['Safe'])
async def Safe_base(self):
    global users
    _file = open(contacts_file,'w',encoding='utf-8')
    json.dump(users,_file,ensure_ascii=False)
    print ('файл cохранен')
    _file.close()

@dp.message_handler(regexp=r'^Add')
async def add_user(message: types.Message):
    global users
    add_message = message.text[4:].split(', ')
    id_user = message["from"]["id"]
    contact = ''
    for data in add_message:
        contact  += data + ';'
    if(id_user not in users.keys()):
        users[id_user] = []
        users[id_user].append(contact)
    else:
        users[id_user].append(contact)
    await message.answer(text=f"Пользователь {add_message[0]} добавлен")

@dp.message_handler(regexp=r'^Search')
async def search_user(message: types.Message):
    global users
    id_user = message["from"]["id"]
    for contact in users[id_user]:
        if(contact.find(message.text[7:])!=-1):
            await message.answer(text=f'Найден контакт {contact}')

@dp.message_handler(regexp=r'^Delete')
async def search_user(message: types.Message):
    global users
    id_user = message["from"]["id"]
    for i in range(len(users[id_user])):
        if(users[id_user][i].find(message.text[7:])!=-1):
            await message.answer(text=f'Удален контакт {users[id_user][i]}')
            del users[id_user][i]
            break


@dp.message_handler(commands=['Test'])
async def test_bot(message:types.Message):
    await message.answer(text='Бот активен')


if __name__ == '__main__':
    print(f'Бот запущен')
    executor.start_polling(dispatcher=dp)
    print(f'Бот остановлен')




