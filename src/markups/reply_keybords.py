from enum import IntEnum, auto
from typing import Optional

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


class JobActions(IntEnum):
    respond = auto()
    buy = auto()
    back = auto()


class JobCbData(CallbackData, prefix="job"):
    action: JobActions
    id: int
    description: str | None = None


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
    kb.button(
        text="🪚 Стройка/отделка",
        callback_data=CategoryCbData(
            action=CategoryActions.details,
            name="clerical",
        ),
    )
    kb.button(
        text="🚚 Доставка",
        callback_data=CategoryCbData(
            action=CategoryActions.details,
            name="trucking",
        ),
    )
    kb.button(
        text="💻 Вэб-разработка",
        callback_data=CategoryCbData(
            action=CategoryActions.details,
            name="webdevelopment",
        ),
    )
    kb.button(
        text="📞 Удаленка",
        callback_data=CategoryCbData(
            action=CategoryActions.details,
            name="virtualassistant",
        ),
    )
    kb.button(
        text="❤️ Уход за здоровьем",
        callback_data=CategoryCbData(
            action=CategoryActions.details,
            name="healthandbeauty",
        ),
    )
    kb.button(
        text="🔖 Прочее",
        callback_data=CategoryCbData(
            action=CategoryActions.details,
            name="house",
        ),
    )
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


def job_details_keyboard(
    description: str,
    pk: int,
) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(
        text="✔️ Откликнуться",
        callback_data=JobCbData(
            action=JobActions.respond,
            id=pk,
            description=description[:30],
        ),
    )

    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)


def payment_kb(pk: int) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(
        text="💳 Оплатить",
        callback_data=JobCbData(
            action=JobActions.buy,
            id=pk,
        ),
    )
    kb.button(
        text="🔙 Назад",
        callback_data=JobCbData(
            action=JobActions.back,
            id=pk,
        ),
    )
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)
