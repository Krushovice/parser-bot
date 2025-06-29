from fastapi import FastAPI, Request
from aiogram.types import Update

from bot import bot, dp
from lifespan import lifespan
from utils.logger import setup_logger

logger = setup_logger(__name__)
app = FastAPI(lifespan=lifespan)


# Маршрут для обработки вебхуков
@app.post("/webhook")
async def webhook(request: Request) -> None:
    logger.info("Received webhook request")
    update = Update.model_validate(
        await request.json(),
        context={"bot": bot},
    )
    await dp.feed_update(bot, update)
    logger.info("Update processed")
