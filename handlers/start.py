from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from keyboards.reply import main_keyboard
from database.models import add_user

router = Router()


@router.message(Command('start'))
async def cmd_start(message: Message):
    add_user(message.from_user.id)
    await message.answer(
"""
👋 Привет!

🤖 Я бот с мотивационными цитатами!

✍️ Напиши:

        - /quote
        
Или нажми на книпку ниже 👇
""", reply_markup=main_keyboard
)
