from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from ..config import Settings

router = Router()
config = Settings()

@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(f"Hello, {message.from_user.username}, I am {config.bot_name}")