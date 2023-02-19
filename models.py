import uuid
from datetime import datetime
from email import message

from sqlalchemy import (
    UUID,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    PrimaryKeyConstraint,
    String,
    text,
)
from sqlalchemy.orm import Mapped, composite, mapped_column, relationship
from sqlalchemy_utils import UUIDType

from database import Base


class UserRDB(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        UUIDType(binary=False), primary_key=True, index=True
    )
    name: Mapped[str] = mapped_column(String(length=255), index=True)
    email: Mapped[str] = mapped_column(String(length=255), unique=True, index=True)
    hash_password: Mapped[str] = mapped_column(String(length=255), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP")
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
    )


class InvalidUserRDB(Base):
    __tablename__ = "invalid_users"

    id: Mapped[uuid.UUID] = mapped_column(
        UUIDType(binary=False), primary_key=True, index=True
    )
    original_user_id: Mapped[uuid.UUID] = mapped_column(
        UUIDType(binary=False), ForeignKey("users.id"), nullable=False
    )
    name: Mapped[str] = mapped_column(String(length=255), index=True)
    email = Column(String(length=255), unique=True, index=True)
    hashed_password = Column(String(length=255))
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP")
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
    )
    original_deleted_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    original_user = relationship("User", back_populates="invalid_user")


class FollowRDB(Base):
    __tablename__ = "follows"

    from_user_id: Mapped[uuid.UUID] = mapped_column(
        UUIDType(binary=False), ForeignKey("users.id"), unique=True, index=True
    )
    to_user_id: Mapped[uuid.UUID] = mapped_column(
        UUIDType(binary=False), ForeignKey("users.id"), unique=True, index=True
    )

    from_user = relationship("User", back_populates="follows")
    to_user = relationship("User", back_populates="follows")
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP")
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
    )
    __table__args__ = PrimaryKeyConstraint(from_user_id, to_user_id)


class FavoriteRDB(Base):
    __tablename__ = "favorites"

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUIDType(binary=False), ForeignKey("users.id"), unique=True
    )
    message_id: Mapped[uuid.UUID] = mapped_column(
        UUIDType(binary=False), ForeignKey("messages.id"), unique=True
    )

    __table__args__ = PrimaryKeyConstraint(user_id, message_id)
    user: Mapped["UserRDB"] = relationship("UserRDB", back_populates="favorites")
    message: Mapped["MessageRDB"] = relationship(
        "MessageRDB", back_populates="favorites"
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP")
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
    )


class ThreadRDB(Base):
    __tablename__ = "threads"

    id: Mapped[uuid.UUID] = mapped_column(
        UUIDType(binary=False), primary_key=True, index=True
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUIDType(binary=False), ForeignKey("users.id"), unique=True
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP")
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
    )
    user = relationship("User", back_populates="threads")


class MessageRDB(Base):
    __tablename__ = "messages"

    id: Mapped[uuid.UUID] = mapped_column(
        UUIDType(binary=False), primary_key=True, index=True
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUIDType(binary=False), ForeignKey("users.id"), unique=True
    )
    thread_id: Mapped[uuid.UUID] = mapped_column(
        UUIDType(binary=False), ForeignKey("threads.id"), unique=True, index=True
    )
    content: Mapped[str] = mapped_column(String(length=255))
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP")
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
    )
    thread = relationship("Thread", back_populates="messages")
    user = relationship("User", back_populates="messages")
