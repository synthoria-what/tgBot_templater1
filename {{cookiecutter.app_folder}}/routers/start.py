from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from config import Settings
from db.services.crud_user import SQLManager

router = Router()
config = Settings()
sql = SQLManager()

@router.message(CommandStart())
async def start_command(message: Message):
    await sql.create_user(message.from_user.username, message.from_user.full_name, message.chat.id)
    await message.answer(f"Hello, {message.from_user.username}, I am {config.bot_name}")