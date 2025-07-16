__all__ = ("router",)

from aiogram import Router

from .job_callback_handlers import router as job_callback_router


router = Router()
router.include_router(job_callback_router)
