from aiogram import Router, F
from aiogram.types import Message
from services.get_quote import get_next_quote_for_user

router = Router()

@router.message(F.text == "Получить цитату")
async def cmd_quote_button(message: Message):
    quote = get_next_quote_for_user(message.from_user.id)
    await message.answer(quote)