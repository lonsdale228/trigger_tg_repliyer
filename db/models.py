from datetime import datetime

from sqlalchemy import BigInteger, Boolean, String, ForeignKey, func
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(AsyncAttrs, DeclarativeBase):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    pass


class Users(Base):
    __tablename__ = "users"

    user_tg_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)
    is_admin: Mapped[bool] = mapped_column(Boolean, nullable=False)
    register_date: Mapped[datetime] = mapped_column(
        server_default=func.now(), nullable=False
    )
    is_banned: Mapped[bool] = mapped_column(Boolean, nullable=False)
    user_details: Mapped["UserDetails"] = relationship(
        "UserDetails", back_populates="user"
    )


class UserDetails(Base):
    __tablename__ = "user_details"

    user_tg_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("users.user_tg_id"), unique=True, nullable=False
    )
    username: Mapped[str | None] = mapped_column(String, nullable=True)
    fullname: Mapped[str | None] = mapped_column(String, nullable=True)

    user: Mapped["Users"] = relationship("Users", back_populates="user_details")