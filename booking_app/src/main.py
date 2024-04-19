# 1.Создать пустую директорию с именем booking_app.
# Создать и активировать виртуальное окружение.
# Добавить файл .gitignore в пустую директорию.
# Установить библиотеки fastapi, uvicorn, pydantic.
# Создать файл requirements.txt добавить все установленные библиотеки.

# 2.Создать директорию src .
# Внутри директории создать файл c именем main.py .
# Создать объект класса FastAPI() . Создать один эндпоинт с get запросом,
# который будет возвращать список из 5 случайных чисел. Числа генерируются с помощью модуля random.
from fastapi import FastAPI
from pydantic import BaseModel, PositiveInt, Field
import random

app = FastAPI()


@app.get("/")
def get_random_numbers():
    random_numbers = [random.randint(1, 100) for number in range(5)]
    return random_numbers


# 3.Создать 3 эндпоинта для get запросов,
# которые возвращают словари. 1 возвращает данные которые прокидываются
# в качестве path params название {item_id} тип int.
# 2 возвращает данные переданные в качестве query params.
# Имена произвольные двух типов int и str.
# 3 возвращает 1 path params тип str и два query params тип int, int

@app.get("/items/{item_id}")
def get_path_params(
        item_id: int
) -> dict:
    return {"item_id": item_id}


@app.get("/items")
def get_query_params(
        name: str,
        item_id: int
) -> dict:
    return {
        "item_id": item_id,
        "name": name
    }


@app.get("/items/{name}")
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


# 4.Используя pydantic создайте класс Actor c полями
# (actor_id int, name str, surname str, age int, sex str)
# Создайте эндпоинт c post запросом который принимает в body (actor: Actors).
# и возвращает актёра с переданными полями в теле запроса.

# 5.Используйте возможности pydantic и провалидируйте поля класса Actor
# следующим образом: actor_id сделайте положительным числом,
# age определите от 0 до 100,
# name и surname сделайте не более 20 символов и не менее 2,
# sex добавьте возможность выбора только male и female .

class Actor(BaseModel):
    actor_id: PositiveInt
    name: str = Field(min_length=2, max_length=20)
    surname: str = Field(min_length=2, max_length=20)
    age: int = Field(ge=0, le=100)
    sex: str = Field(..., choices=["male", "female"])


@app.post("/actor", response_model=Actor)
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
