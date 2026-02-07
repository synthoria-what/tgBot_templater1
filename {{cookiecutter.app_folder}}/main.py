import asyncio
from aiogram import Bot, Dispatcher
from config import Settings
from routers import routers
from db.core import init_db

async def start_bot():
    bot = Bot(Settings().bot_token)
    dp = Dispatcher()
    for router in routers:
        dp.include_router(router)
    await init_db()
    await dp.start_polling(bot)
    
    
    
if __name__ == "__main__":
    print("bot started")
    asyncio.run(start_bot())
    print("bot closed")