from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from services.quote_list import quotes
from services.get_quote_index import get_quote_index
from database.models import save_quote_index

router = Router()

@router.message(Command("quote"))
async def cmd_quote(message: Message):
    quote_index = get_quote_index(message.from_user.id)
    if quote_index is None:
        quote_index = 0

    if quote_index >= len(quotes):
        quote_index = 0

    quote = quotes[quote_index]

    next_quote_index = quote_index + 1
    if next_quote_index >= len(quotes):
        next_quote_index = 0

    save_quote_index(message.from_user.id, next_quote_index)

    await message.answer(quote)