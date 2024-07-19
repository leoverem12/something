from aiogram.utils.keyboard import InlineKeyboardBuilder




# Inline клавіатура для списку фільмів
def build_films_keyboard(films: list):
   builder = InlineKeyboardBuilder()
   for index, film in enumerate(films):
       builder.button(text=film.get("title"), callback_data=f"film_{index}")
   return builder.as_markup()