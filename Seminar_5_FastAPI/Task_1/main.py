# Создать API для управления списком задач. Приложение должно иметь
# возможность создавать, обновлять, удалять и получать список задач.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс Task с полями id, title, description и status.
# Создайте список tasks для хранения задач.
# Создайте маршрут для получения списка задач (метод GET).
# Создайте маршрут для создания новой задачи (метод POST).
# Создайте маршрут для обновления задачи (метод PUT).
# Создайте маршрут для удаления задачи (метод DELETE).
# Реализуйте валидацию данных запроса и ответа.


from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uvicorn


app = FastAPI()


class Task(BaseModel):
    id_: int
    title: str
    description: Optional[str] = None
    status: str


statuses = ["to do", "in progress", "done"]
tasks = []
for i in range(1, 6):
    id = i
    title = "name_" + str(i)
    description = "description_" + str(i) * 3
    status = choice(statuses)
    data = {"id": id, "title": title, "description": description, "status": status}
    task = Task(**data)
    tasks.append(task)


@app.get('/')
async def root():
    return {"task_list": tasks}


@app.post('/tasks/')
async def creat_task(task: Task):
    tasks.append(task)
    return task


@app.put('/tasks/{id_task}')
async def update_task(id_task: int, task: Task):
    for i in range(len(tasks)):
        if tasks[i].id == id_task:
            tasks[i] = task    
    return {'id_task': id_task, 'task': task}


@app.delete('/tasks/{id_task}')
async def delete_task(id_task: int):
    for task in tasks:
        if task.id == id_task:
            tasks.remove(task)    
    return {'id_task': id_task}


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000)
