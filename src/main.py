from fastapi import FastAPI, Request

from bot import bot, dp
from lifespan import lifespan
from utils.logger import setup_logger

logger = setup_logger(__name__)
app = FastAPI(lifespan=lifespan)


# Маршрут для обработки вебхуков
@app.post("/webhook")
async def webhook(request: Request) -> None:
    logger.info("Received webhook request")
    update = await request.json()  # Получаем данные из запроса
    # Обрабатываем обновление через диспетчер (dp) и передаем в бот
    await dp.feed_update(bot, update)
    logger.info("Update processed")
