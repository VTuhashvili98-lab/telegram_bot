import sqlite3

with sqlite3.connect("bot.db") as conn:
    cursor = conn.cursor()
    cursor.execute("""
    SELECT last_quote_index FROM users
    """)

    row = cursor.fetchone()

print(row)