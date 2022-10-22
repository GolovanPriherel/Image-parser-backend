import logging

from src.models.clickhouse.base_model import get_pg_session
from src.models.clickhouse.images_info_model import ImagesInfoModel


class CreateDataBase:
    def __init__(self):
        self.images_info_table = ImagesInfoModel.__table__

    def execute(self):
        self.pg_session = get_pg_session()
        try:
            self.processing()
        except Exception as e:
            raise Exception(e)
        finally:
            self.pg_session.close()

    def processing(self):
        self.images_info_table.create()
        logging.info(f"База данных {ImagesInfoModel} успешно создана")
