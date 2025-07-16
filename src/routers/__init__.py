__all__ = ("router",)


from aiogram import Router

from .user_handlers import router as user_router
from .payment_handlers import router as payment_router
from .callbacks import router as callbacks_router

router = Router()
router.include_routers(
    user_router,
    payment_router,
    callbacks_router,
)
