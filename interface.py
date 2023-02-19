from pydantic import BaseModel


class CreateUser(BaseModel):
    name: str
    email: str
    password: str


class TimeLineView(BaseModel):
    threads: list["ThreadView"]


class ThreadView(BaseModel):
    messages: list["MessageView"]


class MessageView(BaseModel):
    content: str
    favorites: 


class FavoriteView(BaseModel):
    user_name: str
