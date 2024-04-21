from fastapi import APIRouter
from pydantic import BaseModel, PositiveInt, Field


class Actor(BaseModel):
    actor_id: PositiveInt
    name: str = Field(min_length=2, max_length=20)
    surname: str = Field(min_length=2, max_length=20)
    age: int = Field(ge=0, le=100)
    sex: str = Field(..., choices=["male", "female"])


router = APIRouter(
    prefix="/users",
    tags=["Auth"]
)


@router.post("", response_model=Actor)
def get_actor() -> Actor:
    actor_db = {
        "actor_id": 1,
        "name": "Brad",
        "surname": "Pitt",
        "age": 50,
        "sex": "male"
    }
    actor = Actor(**actor_db)
    return actor
