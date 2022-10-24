import logging

from src.models.postgres.base_model import get_pg_session
from src.models.postgres.images_info_model import ImagesInfoModel


class DropDatabase:
    def __init__(self):
        self.images_info_table = ImagesInfoModel.__table__

    def execute(self):
        self.pg_session = get_pg_session()

        try:
            self.processing()
            self.pg_session.commit()
        except Exception as e:
            raise Exception(e)
        finally:
            self.pg_session.close()

    def processing(self):
        self.images_info_table.drop()
