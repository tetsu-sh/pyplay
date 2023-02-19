import uuid
from dataclasses import dataclass

from fastapi import Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from di import get_db
from interface import CreateUser, ThreadView, TimeLineView
from repository import FollowRepository, User, UserRepository
from utils import gen_uuid, hash_password


class UserUseCase:
    def __init__(self, session: Session, user_repository: UserRepository) -> None:
        self.session = session
        self.user_repository = user_repository

    def create_user(self, req: CreateUser) -> None:
        id = gen_uuid()
        hashed_password = hash_password(req.password)
        user = User(
            id=id, name=req.name, email=req.email, hash_password=hashed_password
        )
        with self.session as session:

            UserRepository(db_session=session).save(user)
            session.commit()

        return


class TimelineUseCase:
    def __init__(
        self,
        session: Session,
        user_repository: UserRepository,
        follow_repository: FollowRepository,
    ) -> None:
        self.session = session
        self.user_repository = user_repository
        self.follow_repository = follow_repository

    def fetch_timeline(self, user_id: str) -> TimeLineView:
        query = TimeLineViewQuery.fetch_timeline(self.session, user_id=user_id)
        TimeLineView([ThreadView() for x in query])
        pass


class TimeLineViewQuery:
    def __init__(self) -> None:
        pass

    def fetch_timeline(self, session: Session, user_id: uuid.UUID):
        qr = session.execute(
            text(
                "SELECT u.name as user_name, m.id as message_id, m.content as content,(SELECT count(fv.message_id) from favorites as fv where m.id=fv.message_id) as favorite_count from messages m join users as u on u.id=m.user_id where m.user_id =(select to_user_id from follows f WHERE f.from_user_id=:id)"
            ),
            {"id": user_id},
        ).all()
        return qr


@dataclass
class TimeLineViewQueryResult:
    user_name: str
    message_id: uuid.UUID
    content: str
    favorite_cont: int
