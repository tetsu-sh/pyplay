import uuid

from passlib.context import CryptContext


def gen_uuid() -> uuid.UUID:
    return uuid.uuid4()


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """covert password to hashed encrypt

    Returns:
        str: hashed_password
    """

    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
