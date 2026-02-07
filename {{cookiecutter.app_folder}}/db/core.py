from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from config import Settings


class Base(DeclarativeBase): pass


engine = create_async_engine(Settings().db_url)
AsyncSessionLocal = async_sessionmaker(engine)


async def init_db():
    async with engine.begin() as con:
        await con.run_sync(Base.metadata.create_all)