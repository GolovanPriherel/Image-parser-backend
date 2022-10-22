from src.operators.postgres.create_database import CreateDataBase

# TODO доделать тесты, чтобы можно было делать тестовые БД

create_database = CreateDataBase()
create_database.execute()
