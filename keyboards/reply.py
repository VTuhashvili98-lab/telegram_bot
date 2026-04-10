from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

mian_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Получить цитату")]
    ],
    resize_keyboard=True
)