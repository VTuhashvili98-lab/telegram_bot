import random
import sqlite3

quotes = [
    "Успех — это сумма маленьких усилий, повторяемых изо дня в день.",
    "Не бойся идти медленно, бойся стоять на месте.",
    "Лучше сделать плохо, чем не сделать никак",
    "Каждый день — это новый шанс стать лучше.",
    "Иногда полезно вернуться туда, где ничего не меняется, чтобы посмотреть, как изменился ты.",
    "Помни, что шаг назад часто бывает лучше, чем стояние на месте."
]


def get_random_quote():
    return random.choice(quotes)


def get_quote(user_id: int):
    with sqlite3.connect("bot.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
        SELECT last_quote_index FROM users WHERE telegram_id = ?
        """, (user_id,))

        row = cursor.fetchone()
        return row[0] if row else None