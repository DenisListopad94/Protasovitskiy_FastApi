from fastapi import APIRouter
import random

router = APIRouter(
    prefix="",
    tags=["Booking"]
)


@router.get("/")
def get_random_numbers():
    random_numbers = [random.randint(1, 100) for number in range(5)]
    return random_numbers


@router.get("/items/{item_id}")
def get_path_params(
        item_id: int
) -> dict:
    return {"item_id": item_id}


@router.get("/items")
def get_query_params(
        name: str,
        item_id: int
) -> dict:
    return {
        "item_id": item_id,
        "name": name
    }


@router.get("/items/{name}")
def get_path_query_params(
        name: str,
        item_id: int,
        elem_id: int
) -> dict:
    return {
        "item_id": item_id,
        "name": name,
        "elem_id": elem_id
    }
