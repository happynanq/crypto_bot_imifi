from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.state import State, StatesGroup
from datetime import datetime
from keyboards.simple_row import make_row_keyboard
import json
from helper.parse_json import get_all_chats
from helper.task_today import pp_task, ret_task
from helper.get_bot import get_bot

router = Router()
class UserState(StatesGroup):
    user_reg = State()
    admin_reg = State()

@router.message(UserState.admin_reg, F.text.lower() == "pip")
async def dice_day(message:Message, state:FSMContext):
    # await message.answer(text="Начался новый день задач!")
    chats = get_all_chats()
    bot = get_bot()
    pp_task()
    print("TASK: ", ret_task() )
    for chat in chats:
        await bot.send_message(chat_id=chat, text="Начался новый день задач! /new_task")

# че да