import sqlite3

def get_quote_index(user_id: int):
    with sqlite3.connect("bot.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
        SELECT last_quote_index FROM users WHERE telegram_id = ?
        """, (user_id,))

        row = cursor.fetchone()
        return row[0] if row else None