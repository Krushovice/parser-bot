import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request

from bot import bot, dp
from core.config import settings
from utils.logger import setup_logger

logger = setup_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Код, выполняющийся при запуске приложения
    webhook_url = settings.get_webhook_url()  # Получаем URL вебхука
    await bot.set_webhook(
        url=webhook_url,
        allowed_updates=dp.resolve_used_update_types(),
        drop_pending_updates=True,
    )
    logger.info(f"Webhook set to {webhook_url}")
    yield  # Приложение работает
    # Код, выполняющийся при завершении работы приложения
    await bot.delete_webhook()
    logger.info("Webhook removed")
