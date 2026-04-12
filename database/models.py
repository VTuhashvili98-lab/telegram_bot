import sqlite3

def add_user(telegram_id: int):
    with sqlite3.connect("bot.db") as conn:
        cursor = conn.cursor()

        cursor.execute("""
        INSERT OR IGNORE INTO users (telegram_id)
        VALUES (?)
        """, (telegram_id,))