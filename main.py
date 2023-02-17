import uuid
from typing import Optional

from fastapi import Depends, FastAPI
from injector import Inject, Injector
from sqlalchemy.orm import Session

import models
from database import SessionLocal, engine
from interface import CreateUser, TimeLineView
from repository import User, UserRepository
from usecase import UserUseCase

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


injector = Injector([get_db(), UserRepository()])


@app.get("/")
async def healthcheck():
    return {"message": "Hello World"}


@app.get("/timeline/", response_model=TimeLineView)
async def get_timeline(user_id: str):
    return


@app.post("/message")
async def create_message(thread_id: Optional[str], user_id: str) -> None:
    return


@app.post("/follow")
async def follow(to_user_id: str, user_id: str) -> None:
    return


@app.post("/user")
async def create_user(req: CreateUser) -> None:
    UserUseCase().create_user(req)
    return


@app.post("/favorite")
async def favo(message_id: str, user_id: str) -> None:
    return
