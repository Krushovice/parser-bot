from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from core.config import settings

bot = Bot(
    token=settings.bot.token,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML),
)
dp = Dispatcher()


async def start_bot():
    try:
        await bot.send_message(
            settings.bot.admin_id,
            f"Я запущен🥳.",
        )
    except:
        pass


async def stop_bot():
    try:
        await bot.send_message(
            settings.bot.admin_id,
            "Бот остановлен",
        )
    except:
        pass
