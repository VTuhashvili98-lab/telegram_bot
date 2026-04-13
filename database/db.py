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