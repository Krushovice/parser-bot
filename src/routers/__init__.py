__all__ = ("router",)


from aiogram import Router

from user_handlers import router as user_router
from payment_handlers import router as payment_router


router = Router()
router.include_routers(user_router, payment_router)
