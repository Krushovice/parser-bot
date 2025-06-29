from contextlib import asynccontextmanager

from fastapi import FastAPI

from bot import bot, dp, start_bot, stop_bot
from core.config import settings
from utils.logger import setup_logger
from routers import router as main_router

logger = setup_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting bot setup...")
    dp.include_router(main_router)
    await start_bot()
    webhook_url = settings.web.get_webhook_url
    await bot.set_webhook(
        url=webhook_url,
        allowed_updates=dp.resolve_used_update_types(),
        drop_pending_updates=True,
    )
    logger.info(f"Webhook set to {webhook_url}")
    yield
    logger.info("Shutting down bot...")
    await bot.delete_webhook()
    await stop_bot()
    logger.info("Webhook deleted")
