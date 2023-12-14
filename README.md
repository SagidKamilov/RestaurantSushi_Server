![Static Badge](https://img.shields.io/badge/FastAPI%20-%20v0.45.0%20-%20green?style=for-the-badge&logo=fastapi&color=darkgreen)
![Static Badge](https://img.shields.io/badge/SQLAlchemy%20-%20v2.0.23%20-%20green?style=for-the-badge&logo=sqlalchemy&color=darkgreen)
![Static Badge](https://img.shields.io/badge/Alembic%20-%20v1.12.1%20-%20green?style=for-the-badge&logo=Alembic&color=darkgreen)
![Static Badge](https://img.shields.io/badge/Pydantic%20-%20v1.2.0%20-%20green?style=for-the-badge&logo=Pydantic&color=darkgreen)
![Static Badge](https://img.shields.io/badge/Uvicorn%20-%20v0.22.0%20-%20green?style=for-the-badge&logo=Uvicorn&color=darkgreen)
![Static Badge](https://img.shields.io/badge/Asyncpg%20-%20v0.29.0%20-%20green?style=for-the-badge&logo=Asyncpg&color=darkgreen)
![Static Badge](https://img.shields.io/badge/DOCKER%20-%20%20-%20green?style=for-the-badge&logo=Docker&color=darkgreen)
# RestaurantSushi_Server

RestaurantSushi_Server - Серверная часть для ресторана суши.
Проект RestaurantSushi_Server представляет собой серверную инфраструктуру на основе чистой архитектуры (луковица), созданную специально для управления данными в ресторане суши. Этот проект обеспечивает надежное и эффективное взаимодействие с базой данных, обработку заказов, управление меню и клиентской информацией.

## Описание проекта

Управление меню: Добавление, обновление и удаление блюд, категорий и других элементов меню.

Управление заказами: Обработка заказов, отслеживание статуса заказа и взаимодействие с клиентскими запросами.

Клиентская информация: Хранение и обработка данных о клиентах, история заказов и предпочтения.

Администрация: Управление сервисом за счет полного контроля над всеми процессами, получаемого через админ-панель.

## Технологии

- **FastAPI**: TaskService_Server основан на FastAPI, современном и высокопроизводительном веб-фреймворке для создания микросервисов с API. По сравнению с аналогами, такими как Flask и Django, FastAPI обеспечивает быстрый и эффективный опыт разработки.

- **SQLAlchemy**: Для взаимодействия с базой данных, TaskService_Server использует SQLAlchemy, мощный инструмент для работы с реляционными базами данных.

- **Alembic**: Миграции базы данных в TaskService_Server управляются с помощью Alembic, что обеспечивает надежное и управляемое изменение структуры данных.

- **Pydantic**: С использованием Pydantic в TaskService_Server обеспечивается удобная и автоматизированная валидация данных, что повышает надежность системы.

- **Uvicorn**: Для запуска и обслуживания веб-приложения используется Uvicorn, обеспечивающий высокую производительность и поддержку асинхронности.

- **Asyncpg**: В качестве асинхронного драйвера для работы с SQLite, TaskService_Server использует AIOSQLITE, что способствует эффективной обработке запросов.

- **Docker**: Приложение легко развертывается и управляется в контейнерной среде с использованием Docker, обеспечивая удобство и консистентность окружения