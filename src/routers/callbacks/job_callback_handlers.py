from aiogram import Router, F
from aiogram.types import CallbackQuery

from markups.reply_keybords import CategoryCbData, CategoryActions
from utils.logger import setup_logger
from utils.parser import get_jobs_by_category

router = Router(name=__name__)
logger = setup_logger(__name__)


@router.callback_query(CategoryCbData.filter(F.action == CategoryActions.details))
async def handle_job_details_button(
    call: CallbackQuery,
    callback_data: CategoryCbData,
):
    category = callback_data.name
    await call.answer()
    tasks = await get_jobs_by_category(category=category)
    try:
        for i in range(5):
            await call.message.answer(
                text=f"""
                     <b>📝 Задание</b>: {tasks[i].get('title')}\n
<b>💰 Бюджет</b>: {tasks[i].get('budget')}\n
<b>📆 Срок выполнения</b>: {tasks[i].get('deadline')}\n                 
            
                     """
            )
    except Exception as e:
        logger.error(e)
