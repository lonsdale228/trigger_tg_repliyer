from datetime import datetime

from sqlalchemy import BigInteger, Boolean, DateTime, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    pass


class Users(Base):
    __tablename__ = "users"

    user_tg_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)
    is_admin: Mapped[bool] = mapped_column(Boolean)
    register_date: Mapped[datetime] = mapped_column(DateTime)
    is_banned: Mapped[bool] = mapped_column(Boolean)
    user_details: Mapped["UserDetails"] = relationship(
        "UserDetails", back_populates="user"
    )


class UserDetails(Base):
    __tablename__ = "user_details"

    user_tg_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("users.user_tg_id"), unique=True, nullable=False
    )
    username: Mapped[str] = mapped_column(String, nullable=True)
    fullname: Mapped[str] = mapped_column(String, nullable=True)

    user: Mapped["Users"] = relationship("Users", back_populates="user_details")