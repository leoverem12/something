from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.utils.markdown import hbold


from ..data import get_films, get_film
from ..keyboards import build_films_keyboard, build_film_details_keyboard




film_router = Router()




#Обробник для команди /films та повідомлення із текстом films
@film_router.message(Command("films"))
@film_router.message(F.text.casefold() == "films")
async def show_films_command(message: Message, state: FSMContext) -> None:
   films = get_films()
   keyboard = build_films_keyboard(films)
   await message.answer(
       text="Виберіть будь-який фільм",
       reply_markup=keyboard,
   )


@film_router.callback_query(F.data.startswith("film_"))
async def show_film_details(callback: CallbackQuery, state: FSMContext) -> None:
   film_id = int(callback.data.split("_")[-1])
   film = get_film(film_id)
   text = f"Назва:{hbold(film.get('title'))}\nОпис:{hbold(film.get('desc'))}\nРейтинг:{hbold(film.get('rating'))}"
   photo_id = film.get('photo')
   url = film.get('url')
#    await callback.message.answer_photo(photo_id)
   await edit_or_answer(callback.message, text, build_film_details_keyboard(url))




async def edit_or_answer(message: Message, text: str, keyboard, *args, **kwargs):
   if message.from_user.is_bot:
       await message.edit_text(text=text, reply_markup=keyboard, **kwargs)
   else:
       await message.answer(text=text, reply_markup=keyboard, **kwargs)
