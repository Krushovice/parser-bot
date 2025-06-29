from aiogram.types import ReplyKeyboardMarkup, WebAppInfo
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from src.core.config import settings


def main_keyboard(user_id: int) -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    # url_applications = f"{settings.BASE_SITE}/applications?user_id={user_id}"
    # url_add_application = (
    #     f"{settings.BASE_SITE}/form?user_id={user_id}&first_name={first_name}"
    # )
    # kb.button(text="🌐 Предложения по работе", web_app=WebAppInfo(url=url_applications))
    kb.button(text="ℹ️ О нас")
    if user_id == settings.ADMIN_ID:
        kb.button(text="🔑 Админ панель")
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)


def back_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="🔙 Назад")
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)
