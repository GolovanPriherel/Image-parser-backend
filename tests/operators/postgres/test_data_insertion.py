import datetime

from src.operators.postgres.data_insertion import DataInsertion

data = [
    {
    "id": 1,
    "image_description": "собака, кошка",
    "image_path": "data/images/animals.png",
    "image_url": "http://yandex.ru",
    "inserted_at": datetime.datetime.now(),
    },
    {
    "id": 1,
    "image_description": "собака, кошка",
    "image_path": "data/images/animals.png",
    "image_url": "http://yandex.ru",
    "inserted_at": datetime.datetime.now(),
    }
]

data_insertion = DataInsertion(data)
data_insertion.execute()
