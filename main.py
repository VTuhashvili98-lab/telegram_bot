import asyncio
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from handlers.start import router as start_router
from handlers.quote import router as quote_router

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')
if not TOKEN:
    raise ValueError("Токен не найден! Проверь .env файл")

dp = Dispatcher()
dp.include_router(start_router)
dp.include_router(quote_router)


async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())