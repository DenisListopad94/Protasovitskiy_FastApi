# 1. Создать пустую в директории src два пакета auth и booking_app.
# Создать внутри auth пакет routers, внутри пакета создать два питоновских файла base и  user_router.
# Настроить роутинг и добавить созданный роутер в файл main.
from fastapi import FastAPI, Request
from src.auth.routers.base import router as auth_router
from src.booking_app.routers.base import router as book_router
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.include_router(auth_router)
app.include_router(book_router)

# 2. Создать директорию templates и добавить два html файла, users.html и base.html.
# Установить модуль Jinja2 и добавить в файл requirements.txt.
# Настроить использование шаблонов в модуле main.

# 3. Создать эндпоинт для get запроса, которые вернёт шаблон users.html
# и передаст в него данные из словаря в users, состоящего из 10 объектов.
# Структура словаря users=[{“id”:1,”first_name”:”some_name”,
# ”last_name”:”some_name”,”age”:23,”email”:”some_email”},{…}].
# Для вывода данных о пользователях используйте тэг {% for %}{% endfor %}

# 4. Используя шаблон users.html добавьте проверку на возраст.
# Выведите пользователей старше 15 и младше 45.
# А также отдельно выведите пользователей с некорректными именами и фамилиями
# (если в них есть символы отличающиеся от латиницы или кириллицы).

templates = Jinja2Templates(directory="templates")


@app.get("/get_template", response_class=HTMLResponse)
def get_html_template(request: Request):
    users = [
        {"id": 1,
         "first_name": "Bob1",
         "last_name": "Bobson",
         "age": 23,
         "email": "Bob@mail.ru"},
        {"id": 2,
         "first_name": "Bill",
         "last_name": "Billson",
         "age": 50,
         "email": "Bill@mail.ru"},
        {"id": 3,
         "first_name": "Will",
         "last_name": "Willson",
         "age": 45,
         "email": "Will@mail.ru"},
    ]
    return templates.TemplateResponse(
        request=request,
        name="users.html",
        context={"users": users}
    )


# 5. Подключите статику к вашему проекту в файле main.
# Создайте файл users.css и скачайте картинку с толпой людей.
# Подключите файл users.css в шаблон users.html,  а также добавьте скачанную картинку.


app.mount("/static", StaticFiles(directory="static"), name="static")
