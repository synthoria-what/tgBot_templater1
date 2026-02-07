from models.user import User
from sqlalchemy import select, insert, update, delete, or_, and_
from ..core import AsyncSessionLocal

class SQLManager:
    def __init__(self, session_factory=AsyncSessionLocal):
        self._session_factory = session_factory

    async def create_user(self, username: str, full_name: str, telegram_chat_id: int) -> User:
        async with self._session_factory() as session:
            new_user = User(username=username, telegram_chat_id=telegram_chat_id, telegram_full_name=full_name)
            
            session.add(new_user)
            await session.commit()
            await session.refresh(new_user)
            
    async def get_user(self, telegram_chat_id: int) -> User:
        async with self._session_factory() as session:
            user = await session.scalar(select(User).
                where(User.telegram_chat_id == telegram_chat_id))
            
            return user
        
    async def update_user(self, telegram_chat_id: int, **kwargs) -> User | None:
        async with self._session_factory() as session:
            user = await session.scalar(select(User).where(User.telegram_chat_id == telegram_chat_id))
            if not user:
                return None
            
            for key, value in kwargs.items():
                if value is not None and hasattr(user, key):
                    setattr(user, key, value)
                    
            await session.commit()
            await session.refresh(user)
            return User
        
    async def delete_user(self, telegram_chat_id: int) -> bool:
        async with self._session_factory() as session:
            user = await session.scalar(select(User).where(User.telegram_chat_id == telegram_chat_id))
            if not user:
                return False
            
            try:
                session.delete(user)
                await session.commit()
                return True
            except Exception:
                return False
                
            