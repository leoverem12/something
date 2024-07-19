from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove


from ..data import get_films
from ..keyboards import build_films_keyboard




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
