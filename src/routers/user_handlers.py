from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message


router = Router(name=__name__)


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    """
    Обрабатывает команду /start.
    """

    pass


# @router.message(F.text == "🔙 Назад")
# async def cmd_back_home(message: Message) -> None:
#     """
#     Обрабатывает нажатие кнопки "Назад".
#     """
#     await greet_user(message, is_new_user=False)
#
#
# @router.message(F.text == "ℹ️ О нас")
# async def about_us(message: Message):
#     kb = app_keyboard(
#         user_id=message.from_user.id, first_name=message.from_user.first_name
#     )
#     await message.answer(get_about_us_text(), reply_markup=kb)
