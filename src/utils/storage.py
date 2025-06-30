import aioredis
import json

REDIS_KEY = "youdo:tasks"


async def save_to_redis(tasks: list[dict]):
    redis = aioredis.from_url("redis://localhost")
    pipe = redis.pipeline()
    for task in tasks:
        pipe.lpush(REDIS_KEY, json.dumps(task))
    pipe.ltrim(REDIS_KEY, 0, 99)  # оставляем только 100 последних
    await pipe.execute()
