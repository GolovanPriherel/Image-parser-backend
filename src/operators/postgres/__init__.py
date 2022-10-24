from src.models.postgres.images_info_model import ImagesInfoSchema
from src.operators.postgres.create_database import CreateDatabase
from src.operators.postgres.data_insertion import DataInsertion
from src.operators.postgres.drop_database import DropDatabase

# data = {
#         "id": 3,
#         "image_title": "семья.png",
#         "image_tags": ["я", "кошка", "батя1", "батя2"],
#         "image_description": "я, моя кошка, папа по имени Коля, второй папа по имени Игорь",
#         "image_path": "data/images/семья.png",
#         "image_url": "http://yandex.ru",
#         "inserted_at": "2022-10-22 14:18:01.898"
#     }
#
# data = ImagesInfoSchema.parse_obj(data)

create_database = CreateDatabase()
data_insertion = DataInsertion()
drop_database = DropDatabase()
