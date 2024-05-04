from sqlalchemy.orm import Session

from src.auth.models import User
from src.auth.schemas.user_schema import (
    UserCreateSchema, UserUpdateSchema
)


def create_user(
        session: Session,
        body: UserCreateSchema
) -> User:
    user = User(
        first_name=body.first_name,
        last_name=body.last_name,
        role=body.role,
    )

    session.add(user)
    session.commit()
    session.refresh(user)
    return user


def get_users(session: Session):
    return session.query(User).all()


def get_user(session: Session, user_id: int):
    return session.query(User).filter(User.id == user_id).first()


def update_user(
        session: Session,
        user_id: int,
        body: UserUpdateSchema
) -> User:
    user = session.query(User).filter(User.id == user_id).first()
    user.first_name = body.first_name
    user.last_name = body.last_name
    user.role = body.role
    session.commit()
    session.refresh(user)
    return user


def delete_user(
        session: Session,
        user_id: int,
):
    user = session.query(User).filter(User.id == user_id).first()
    session.delete(user)
    session.commit()
