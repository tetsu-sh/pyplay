import hashlib
import re
import uuid
from dataclasses import dataclass
from typing import final

from injector import inject
from pydantic import BaseModel, validator
from sqlalchemy import text
from sqlalchemy.orm import Session

from models import UserRDB

EMAIL_REGRESSION_PATTERN = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"


class EmailInvalidExecption(Exception):
    def __init__(self, message: str) -> None:
        print(f"{message}")


class User(BaseModel):
    id: uuid.UUID
    name: str
    email: str
    hash_password: str

    @validator("email")
    def email_match(cls, v: str) -> str:
        if not re.match(EMAIL_REGRESSION_PATTERN, v):
            raise EmailInvalidExecption(message="invalid email pattern. use")
        return v


class UserRepository:
    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session

    def save(self, user: User) -> None:
        self.db_session.execute(
            text(
                f"""
        INSERT INTO users(id,name,hash_password,email) VALUES(:id,:name,:hash_password,:email)
        """
            ),
            {
                "id": user.id.hex,
                "name": user.name,
                "hash_password": user.hash_password,
                "email": user.email,
            },
        )


class Follow(BaseModel):
    from_user_id: uuid.UUID
    to_user_id: uuid.UUID


class FollowRepository:
    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session

    def save(self, follow: Follow) -> None:
        self.db_session.execute(
            text(
                f"""
        INSERT INTO users(from_user_id,to_user_id) VALUES(:from_user_id,:to_user_id)
        """
            ),
            {
                "from_user_id": follow.from_user_id,
                "to_user_id": follow.to_user_id,
            },
        )


class Message(BaseModel):
    id: uuid.UUID
    thread_id: uuid.UUID
    user_id: uuid.UUID
    content: str


class Thread(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID


class ThreadRepository:
    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session

    def save_first_message(self, message: Message) -> None:
        self.db_session.execute(
            text(
                f"""
        INSERT INTO users(from_user_id,to_user_id) VALUES(:from_user_id,:to_user_id)
        """
            ),
            {
                "from_user_id": follow.from_user_id,
                "to_user_id": follow.to_user_id,
            },
        )
    def save_message(self,thread:Thread,message:Message):
       self.db_session.execute(
            text(
                f"""
        INSERT INTO users(from_user_id,to_user_id) VALUES(:from_user_id,:to_user_id)
        """
            ),
            {
                "from_user_id": follow.from_user_id,
                "to_user_id": follow.to_user_id,
            }, 
