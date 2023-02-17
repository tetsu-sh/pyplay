import hashlib
import re
import uuid
from dataclasses import dataclass
from typing import final

import bcrypt
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

    @validator("hash_password", check_fields=False)
    def hash_password(cls, v: str) -> str:
        hashed_password = bcrypt.hashpw(password=v, salt=bcrypt.gensalt(10))
        return hashed_password


class UserRepository:
    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session

    def save(self, user: User) -> None:
        self.db_session.execute(
            text(
                f"""
        INSERT INTO users(id,name,hash_password,email) VALUES(:user.id,:user.name,user.hash_password,user.email);
        """
            )
        )
