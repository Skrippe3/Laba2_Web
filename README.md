# Laba2_Web
Описание проекта

В рамках лабораторной работы был реализован REST API сервис для управления задачами.
Сервер принимает HTTP-запросы, взаимодействует с базой данных PostgreSQL и возвращает ответы в формате JSON.

Приложение реализовано на языке Python с использованием фреймворка Flask.
Для работы с базой данных используется SQLAlchemy ORM, а для управления схемой базы данных — Flask-Migrate.

Приложение контейнеризировано с использованием Docker и запускается через Docker Compose.

Технологический стек

В проекте используются следующие технологии:

Python

Flask

SQLAlchemy

Flask-Migrate

PostgreSQL

Docker

Docker Compose

Архитектура приложения

Приложение реализует REST API для сущности Task.

Каждая задача содержит следующие поля:

id — уникальный идентификатор (UUID)

title — название задачи

description — описание задачи

status — статус задачи

created_at — дата создания

updated_at — дата обновления

deleted_at — поле для мягкого удаления (soft delete)

Удаление реализовано через soft delete — запись не удаляется физически из базы данных, а помечается временем удаления.

Запуск проекта
1. Клонировать репозиторий
git clone <repository_url>
cd lab2-flask-rest
2. Создать файл .env

Пример содержимого:

FLASK_APP=run.py
FLASK_ENV=development
DB_HOST=postgres
DB_PORT=5432
DB_NAME=wp_labs
DB_USER=student
DB_PASSWORD=student_secure_password
PORT=4200
3. Запуск приложения

Запуск осуществляется через Docker Compose:

docker compose up --build

После запуска сервер будет доступен по адресу:

http://localhost:4200
API endpoints
Создание задачи

POST /tasks

Пример запроса:

{
  "title": "Task demo",
  "description": "Demo task",
  "status": "new"
}
Получение списка задач

GET /tasks?page=1&limit=10

Ответ содержит:

список задач (data)

метаданные пагинации (meta)

Пример ответа:

{
  "data": [
    {
      "id": "uuid",
      "title": "Task demo",
      "description": "Demo task",
      "status": "new"
    }
  ],
  "meta": {
    "total": 1,
    "page": 1,
    "limit": 10,
    "totalPages": 1
  }
}
Получение задачи по ID

GET /tasks/{id}

Полное обновление задачи

PUT /tasks/{id}

Пример:

{
  "title": "Updated task",
  "description": "Updated description",
  "status": "done"
}
Частичное обновление

PATCH /tasks/{id}

Пример:

{
  "status": "in_progress"
}
Удаление задачи

DELETE /tasks/{id}

Удаление реализовано через soft delete.
Запись не удаляется из базы данных, а помечается полем deleted_at.

После удаления задача не возвращается в списке и не доступна по ID.

Миграции базы данных

Для управления схемой базы данных используются миграции Flask-Migrate.

Основные команды:

flask db init
flask db migrate -m "create tasks table"
flask db upgrade
Тестирование API

Для тестирования можно использовать:

PowerShell (Invoke-RestMethod)

curl

Postman

Пример запроса:

Invoke-RestMethod -Method GET `
  -Uri "http://localhost:4200/tasks?page=1&limit=10"
Итог

В результате лабораторной работы был реализован REST API сервис с использованием Flask и PostgreSQL.
Приложение поддерживает CRUD операции, пагинацию и мягкое удаление записей.
Сервис полностью контейнеризирован и может быть запущен через Docker Compose.
