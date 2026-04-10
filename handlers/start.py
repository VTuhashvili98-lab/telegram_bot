from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from keyboards.reply import mian_keyboard

router = Router()


@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer(
"""
👋 Привет!

🤖 Я бот с мотивационными цитатами!

✍️ Напиши:

        - /quote
""", reply_markup=mian_keyboard
)
