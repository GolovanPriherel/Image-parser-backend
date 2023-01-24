### Миграции alembic

- Инициализация миграций `alembic init migrations`
- Создание записи о миграции `alembic revision -m "create <table_name> table"`
- Накатить миграции до последней записи `alembic upgrade head`
- Откатить миграции на 1 `alembic downgrade -1`
- Выгрузка схемы для тестов `alembic upgrade head --sql > migrations/schema.sql`