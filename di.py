from injector import Injector, inject

from database import SessionLocal
from repository import UserRepository


# Dependency
@inject
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def config():
    injector = Injector()
