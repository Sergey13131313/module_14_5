import logging
import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from config import *
from crud_functions import *

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_API)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет я бот помогающий твоему здоровью.')


class UserSRegistrationState(StatesGroup):
    user_name = State()
    email = State()
    age = State()
    balance = State()


@dp.message_handler(text='Регистрация')
async def sing_up(message: types.Message):
    await message.answer('Введите имя пользователя (только латинский алфаыит):')
    await UserSRegistrationState.user_name.set()


@dp.message_handler(state=UserSRegistrationState.user_name)
async def set_username(message: types.Message, state: FSMContext):
    await state.update_data(one=message.text)
    date = await state.get_data()
    if not date.get('one').isascii():
        await message.answer('Только лаьинские буквы')
    elif is_included(date.get('one')):
        await message.answer('Такой пользователь уже существует, введите имя пользователя (только латинский алфаыит):')
    else:
        await message.answer('Введите адрес почты:')
        await UserSRegistrationState.email.set()


@dp.message_handler(state=UserSRegistrationState.email)
async def set_email(message: types.Message, state: FSMContext):
    await state.update_data(two=message.text)
    date = await  state.get_data()
    if not is_email(date.get('two')):
        await message.answer('Не корректный адрес!')
    else:
        await message.answer('Введите свой возраст (целое число):')
        await UserSRegistrationState.age.set()

@dp.message_handler(state=UserSRegistrationState.age)
async def set_age(message: types.Message, state: FSMContext):
    await state.update_data(three=message.text)
    date = await state.get_data()
    if not date.get('three').isdigit():
        await message.answer('Только целое число.')
    else:
        add_user(date['one'], date['two'], date['three'])
        await state.finish()



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
