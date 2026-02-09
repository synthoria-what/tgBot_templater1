from sqlalchemy.orm import Mapped, mapped_column
from ..core import Base
from datetime import datetime
from dataclasses import dataclass


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    role: Mapped[str] = mapped_column(default="user")
    username: Mapped[str] = mapped_column(unique=True, nullable=True)
    telegram_chat_id: Mapped[int] = mapped_column(unique=True)
    telegram_full_name: Mapped[str] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)