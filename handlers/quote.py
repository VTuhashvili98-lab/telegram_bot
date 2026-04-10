from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from services.quotes import get_random_quote

router = Router()

@router.message(Command("quote"))
async def cmd_quote(message: Message):
    quote = get_random_quote()
    await message.answer(quote)