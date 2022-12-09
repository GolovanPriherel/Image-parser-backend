import logging
from typing import List

from src.models.postgres.base_model import get_pg_session
from src.models.postgres.images_info_model import ImagesInfoModel, ImagesInfoSchema


class InsertImagesInfo:
    def __init__(self):
        self.images_info_table = ImagesInfoModel.__table__
        self._data = []

    def execute(self, data: List[ImagesInfoSchema]):
        self._data = data
        with get_pg_session() as pg_session:
            try:
                self.processing(pg_session)
                pg_session.commit()
            except Exception as e:
                raise Exception(e)
            finally:
                pg_session.close()

    def processing(self, pg_session):
        for element in self._data:
            pg_session.execute(
                self.images_info_table.insert().values(element.dict())
            )
