import sqlite3


def init_db():
    with sqlite3.connect("bot.db") as conn:
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id INTEGER UNIQUE,
        is_subscribed INTEGER DEFAULT 0,
        send_time TEXT,
        last_quote_index INTEGER DEFAULT 0
        )
        """)


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


def get_quote_index(user_id: int):
    with sqlite3.connect("bot.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
        SELECT last_quote_index FROM users WHERE telegram_id = ?
        """, (user_id,))

        row = cursor.fetchone()
        return row[0] if row else None