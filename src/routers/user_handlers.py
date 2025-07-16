from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message

from markups.reply_keybords import main_keyboard, job_category_keyboard


router = Router(name=__name__)


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    """
    Обрабатывает команду /start.
    """

    await message.answer(
        f"Добро пожаловать, <b>{message.from_user.full_name}</b>!\n"
        "Чем я могу помочь вам сегодня?",
        reply_markup=main_keyboard(user_id=message.from_user.id),
    )


@router.message(F.text == "🌐 Предложения по работе")
async def handle_job_button(message: Message) -> None:

    await message.answer(
        "Выберите категорию:",
        reply_markup=job_category_keyboard(),
    )


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
