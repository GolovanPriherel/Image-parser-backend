import logging
from typing import List, Dict

from src.models.postgres.base_model import get_pg_session
from src.models.postgres.rule34_images_info import Rule34ImagesInfoModel, Rule34ImagesInfoListSchema


class Rule34InsertImagesInfo:
    def __init__(self):
        self.rule34_images_info = Rule34ImagesInfoModel
        self._data = []

    def execute(self, data: dict):
        self._data = data
        with get_pg_session() as pg_session:
            try:
                self.processing(pg_session)
                pg_session.commit()
            except Exception as e:
                raise Exception(e)

    def processing(self, pg_session):
        for element in self._data:
            logging.warning(element)
            pg_session.merge(Rule34ImagesInfoModel().fill(**element))
            # pg_session.execute(
            #     self.rule34_images_info.insert().values(element.dict())
            # )
