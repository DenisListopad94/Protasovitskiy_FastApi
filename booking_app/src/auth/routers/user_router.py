from fastapi import APIRouter, Depends, status
from src.auth.services.service import (
    create_user,
    get_users,
    get_user,
    update_user,
    delete_user,
)
from sqlalchemy.orm import Session
from src.database import SessionLocal
from src.auth.schemas.user_schema import (
    UserCreateSchema,
    UserUpdateSchema,
    UserReadSchema,
)

router = APIRouter(
    prefix="/users",
    tags=["Auth"]
)


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


@router.post(
    "",
    response_model=UserCreateSchema,
)
def create_user_handler(
        body: UserCreateSchema,
        session: Session = Depends(get_session),
):
    return create_user(
        session=session,
        body=body,
    )


@router.get(
    "",
    response_model=list[UserReadSchema]
)
def read_users_handler(session: Session = Depends(get_session)):
    return get_users(
        session=session,
    )


@router.get(
    "/{user_id}",
    response_model=UserReadSchema | None
)
def read_user_handler(
        user_id: int,
        session: Session = Depends(get_session)
):
    return get_user(
        session=session,
        user_id=user_id
    )


@router.put(
    "/{user_id}",
    response_model=UserUpdateSchema
)
def update_user_handler(
        user_id: int,
        body: UserUpdateSchema,
        session: Session = Depends(get_session)
):
    return update_user(
        session=session,
        user_id=user_id,
        body=body
    )


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_user_handler(
        user_id: int,
        session: Session = Depends(get_session)
):
    delete_user(
        session=session,
        user_id=user_id,
    )
