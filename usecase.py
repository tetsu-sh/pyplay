import uuid

from injector import inject
from sqlalchemy.orm import Session

from interface import CreateUser
from repository import User, UserRepository


class UserUseCase:
    @inject
    def __init__(self, session: Session, user_repository: UserRepository) -> None:
        self.session = session
        self.user_repository = user_repository

    def create_user(self, req: CreateUser) -> None:
        id = uuid.uuid4()
        user = User(
            id=id,
            name=req.name,
            email=req.email,
        )
        with self.session as session:
            UserRepository(db_session=session).save(user)
        return
