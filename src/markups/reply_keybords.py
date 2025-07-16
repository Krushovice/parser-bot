from enum import IntEnum, auto

from aiogram.filters.callback_data import CallbackData
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from src.core.config import settings


class CategoryActions(IntEnum):
    details = auto()
    back = auto()


class CategoryCbData(CallbackData, prefix="cat"):
    action: CategoryActions
    name: str


def main_keyboard(user_id: int) -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    # url_applications = f"{settings.BASE_SITE}/applications?user_id={user_id}"
    # url_add_application = (
    #     f"{settings.BASE_SITE}/form?user_id={user_id}&first_name={first_name}"
    # )
    kb.button(text="🌐 Предложения по работе")

    kb.button(text="ℹ️ О нас")
    if user_id == settings.bot.admin_id:
        kb.button(text="🔑 Админ панель")
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)


def back_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="🔙 Назад")
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)


def job_category_keyboard() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(
        text="🛠 Tехремонт",
        callback_data=CategoryCbData(
            action=CategoryActions.details,
            name="techrepair",
        ),
    )
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)
