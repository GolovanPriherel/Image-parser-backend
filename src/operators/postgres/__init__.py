from src.operators.postgres.create_database import CreateDatabase
from src.operators.postgres.data_insertion import InsertImagesInfo
from src.operators.postgres.drop_database import DropDatabase
from src.operators.postgres.rule34_data_insertion import Rule34InsertImagesInfo
from src.operators.postgres.rule34_urls_insertion import Rule34InsertURLS

create_database = CreateDatabase()
data_insertion = InsertImagesInfo()
rule34_insertion = Rule34InsertImagesInfo()
drop_database = DropDatabase()
rule34_urls_insertion = Rule34InsertURLS()
