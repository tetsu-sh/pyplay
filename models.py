import uuid
from datetime import datetime

from sqlalchemy import UUID, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class UserRDB(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)


class InvalidUserRDB(Base):
    __tablename__ = "invalid_users"

    id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, index=True)
    original_user_id: Mapped[uuid.UUID] = mapped_column(
        UUID, ForeignKey("User.id"), nullable=False
    )
    name: Mapped[str] = mapped_column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    original_deleted_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    original_user = relationship("User", back_populates="invalid_user")


class FollowRDB(Base):
    __tablename__ = "follows"

    id = Column(Integer, primary_key=True, index=True)
    from_user_id = Column(String, ForeignKey("User.id"), unique=True, index=True)
    to_user_id = Column(String, ForeignKey("User.id"), unique=True, index=True)

    from_user = relationship("User", back_populates="follows")
    to_user = relationship("User", back_populates="follows")
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)


class FavoriteRDB(Base):
    __tablename__ = "favorite"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("User.id"), unique=True, index=True)
    message_id = Column(String, ForeignKey("Message.id"), unique=True, index=True)
    # complex index


class ThreadRDB(Base):
    __tablename__ = "thread"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("User.id"), unique=True, index=True)


class MessageRDB(Base):
    __tablename__ = "message"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("User.id"), unique=True, index=True)
    thread_id = Column(String, ForeignKey("Thread.id"), unique=True, index=True)
    content: Mapped[str] = mapped_column(String)
