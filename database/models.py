import sqlite3

def add_user(telegram_id: int):
    with sqlite3.connect("bot.db") as conn:
        cursor = conn.cursor()

        cursor.execute("""
        INSERT OR IGNORE INTO users (telegram_id)
        VALUES (?)
        """, (telegram_id,))


def save_quote_index(user_id: int, quote_index: int):
    with sqlite3.connect("bot.db") as conn:
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE users
        SET last_quote_index = ?
        WHERE telegram_id = ?
        """, (quote_index, user_id))