from aiogram import Router, F
from aiogram.types import CallbackQuery

from markups.reply_keybords import (
    CategoryCbData,
    CategoryActions,
    job_details_keyboard,
    JobCbData,
    JobActions,
    payment_kb,
)
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
            
                     """,
                reply_markup=job_details_keyboard(
                    description=tasks[i].get("title"),
                    pk=i,
                ),
            )
    except Exception as e:
        logger.error(e)


@router.callback_query(JobCbData.filter(F.action == JobActions.respond))
async def handle_job_respond_button(
    call: CallbackQuery,
    callback_data: JobCbData,
):
    await call.answer()
    await call.message.answer(
        text=f"""
            <b>📝 Задание</b>: {callback_data.description}\n
<b>Купить доступ❓</b>                 

                         """,
        reply_markup=payment_kb(pk=callback_data.id),
    )


@router.callback_query(JobCbData.filter(F.action == JobActions.buy))
async def handle_job_buy_button(
    call: CallbackQuery,
    callback_data: JobCbData,
):
    await call.answer()


@router.callback_query(JobCbData.filter(F.action == JobActions.back))
async def handle_job_buy_button(
    call: CallbackQuery,
    callback_data: JobCbData,
):
    await call.answer()
