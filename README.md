# Стартовый шаблон для Telegram бота на aiogram 3 с PostgreSQL
## Структура проекта

```
bot_project/
├── bot/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── handlers/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── admin/
│   │       ├── __init__.py
│   │       ├── main.py
│   │       ├── stats.py
│   │       ├── users.py
│   │       ├── broadcast.py
│   │       └── settings.py
│   ├── keyboards/
│   │   ├── __init__.py
│   │   ├── reply.py
│   │   └── admin.py
│   ├── middlewares/
│   │   ├── __init__.py
│   │   ├── db.py
│   │   └── admin.py
│   ├── states/
│   │   ├── __init__.py
│   │   └── admin.py
│   └── utils/
│       ├── __init__.py
│       ├── commands.py
│       └── admin.py
├── database/
│   ├── __init__.py
│   ├── engine.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   └── user.py
│   └── repositories/
│       ├── __init__.py
│       ├── base.py
│       └── user.py
├── alembic/
│   ├── versions/
│   ├── alembic.ini
│   ├── env.py
│   └── script.py.mako
├── docker-compose.yml
├── .env.example
├── requirements.txt
└── README.md
```

### 🔑 Ключевые особенности:

1. Полностью асинхронная архитектура - использует SQLAlchemy 2.0 с asyncpg
2. Паттерн Repository - инкапсулирует логику работы с БД
3. Middleware система - автоматически создает сессии БД и регистрирует пользователей
4. Alembic миграции - версионирование схемы БД
5. Docker Compose - быстрый запуск PostgreSQL и Redis
6. Pydantic настройки - типизированная конфигурация через .env

```bash
# 1. Создайте структуру проекта
mkdir bot_project && cd bot_project

# 2. Скопируйте файлы из шаблона

# 3. Настройте окружение
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 4. Запустите БД
docker-compose up -d

# 5. Создайте .env из примера
cp .env.example .env
# Добавьте ваш BOT_TOKEN

# 6. Создайте первую миграцию
alembic revision --autogenerate -m "init"
alembic upgrade head

# 7. Запустите бота
python -m bot.main
```
