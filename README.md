![Static Badge](https://img.shields.io/badge/FastAPI%20-%20v0.45.0%20-%20green?style=for-the-badge&logo=fastapi&color=darkgreen)
![Static Badge](https://img.shields.io/badge/SQLAlchemy%20-%20v2.0.23%20-%20green?style=for-the-badge&logo=sqlalchemy&color=darkgreen)
![Static Badge](https://img.shields.io/badge/Alembic%20-%20v1.12.1%20-%20green?style=for-the-badge&logo=Alembic&color=darkgreen)
![Static Badge](https://img.shields.io/badge/Pydantic%20-%201.2.0%20-%20green?style=for-the-badge&logo=Pydantic&color=darkgreen)
![Static Badge](https://img.shields.io/badge/Uvicorn%20-%200.22.0%20-%20green?style=for-the-badge&logo=Uvicorn&color=darkgreen)
![Static Badge](https://img.shields.io/badge/Asyncpg%20-%200.29.0%20-%20green?style=for-the-badge&logo=Asyncpg&color=darkgreen)

# RestaurantSushi_Server
### Серверная часть для ресторана суши

Проект представляет собой серверную часть для ресторана суши, разработанную с использованием SQLAlchemy, Pydantic и FastAPI.


### Описание

Этот проект создан для управления данными и операциями на стороне сервера ресторана суши. 
Он предоставляет API для выполнения различных функций, таких как управление меню, заказы, и клиентской информацией.


### Технологии

- **FastAPI**: FastAPI - современный, быстрый (в сравнении с Flask, Django), веб-фреймворк для создания микросервисов с API. 
- **SQLAlchemy**: SQLAlchemy - библиотека для работы с базами данных в Python. Она предоставляет высокоуровневый API для взаимодействия с различными СУБД.
- **Pydantic**: Pydantic - библиотека для проверки данных и сериализации объектов Python. Она интегрируется хорошо с FastAPI для валидации запросов и ответов API.
- **Alembic


### Установка

1. Клонировать репозиторий:

    ```bash
    git clone https://github.com/ваш-пользователь/ваш-репозиторий.git
    ```

2. Установить зависимости:

    ```bash
    pip install -r requirements.txt.txt
    ```

3. Запустить сервер:

    ```bash
    uvicorn main:app --reload
    ```



### Использование

После установки и запуска сервера, API будет доступно по адресу http://localhost:8000/docs для интерактивной документации с использованием Swagger UI. 
Также, можно использовать ручки API напрямую.
