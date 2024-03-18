# Создать API для обновления информации о пользователе в базе данных.
# Приложение должно иметь возможность принимать PUT запросы с данными
# пользователей и обновлять их в базе данных.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте маршрут для добавления нового пользователя (метод POST).
# Реализуйте валидацию данных запроса и ответа.
# Создайте маршрут для обновления информации о пользователе (метод PUT).
# Создайте маршрут для удаления информации о пользователе (метод DELETE).
# Создайте HTML шаблон для отображения списка пользователей. Шаблон должен
# содержать заголовок страницы, таблицу со списком пользователей и кнопку для
# добавления нового пользователя.
# Создайте маршрут для отображения списка пользователей (метод GET).
# Реализуйте вывод списка пользователей через шаблонизатор Jinja.


from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Optional
import uvicorn
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory="templates")


class User(BaseModel):
    id_: int
    name: str
    email: Optional[str] = None
    password: str


users = [
    User(id_=1, name="Александр", email="alex@mail.ru", password="123456"),
    User(id_=2, name="Сергей", email="serg@gmail.com", password="qwerty"),
    User(id_=3, name="Владимир", email="vlad@yandex.ru", password="1qaz2wsx"),
    User(id_=4, name="Антон", email="anton@mail.ru", password="1q2w3e4r"),
    User(id_=5, name="Дмитрий", email="dima@yandex.ru", password="wasdfqwe"),
    User(id_=6, name="Алексей", email="aleks@gmail.com", password="2wqe312w"),
]


@app.get('/root')
async def root():
    return users


@app.get("/", response_class=HTMLResponse)
async def get_users(request: Request):
    return templates.TemplateResponse("index.html", {"request": request,
                                                     "users": users})


@app.post('/user/')
async def creat_user(user: User):
    users.append(user)
    return user


@app.put('/user/{id_}')
async def update_user(id_: int, user: User):
    for i in range(len(users)):
        if users[i].id_ == id_:
            users[i] = user
    return {'id_': id_, 'user': user}


@app.delete('/user/{id_}')
async def delete_user(id_: int):
    for us in users:
        if us.id_ == id_:
            users.remove(us)
    return {'id_': id_}


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000)
