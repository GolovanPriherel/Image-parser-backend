from src.operators.postgres.create_database import CreateDatabase
from src.operators.postgres.data_insertion import DataInsertion
from src.operators.postgres.drop_database import DropDatabase

create_database = CreateDatabase()
data_insertion = DataInsertion()
drop_database = DropDatabase()
