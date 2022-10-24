from src.operators.postgres.create_database import CreateDatabase

# TODO доделать тесты, чтобы можно было делать тестовые БД

create_database = CreateDatabase()
create_database.execute()
