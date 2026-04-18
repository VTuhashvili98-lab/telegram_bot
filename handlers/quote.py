from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from services.get_quote import get_next_quote_for_user

router = Router()

@router.message(Command("quote"))
async def cmd_quote(message: Message):
    quote = get_next_quote_for_user(message.from_user.id)
    await message.answer(quote)