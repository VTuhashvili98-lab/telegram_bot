from database.db import get_quote_index
from services.quote_list import quotes
from database.db import save_quote_index

def get_next_quote_for_user(user_id: int) -> str:
    quote_index = get_quote_index(user_id)

    if quote_index is None:
        quote_index = 0

    if quote_index >= len(quotes):
        quote_index = 0

    quote = quotes[quote_index]

    next_index = quote_index + 1
    if next_index >= len(quotes):
        next_index = 0

    save_quote_index(user_id, next_index)

    return quote