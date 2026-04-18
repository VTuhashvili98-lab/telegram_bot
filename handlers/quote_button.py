from aiogram import Router, F
from aiogram.types import Message
from services.quote_list import get_random_quote

router = Router()

@router.message(F.text == "Получить цитату")
async def cmd_quote_button(message: Message):
    quote = get_random_quote()
    await message.answer(quote)