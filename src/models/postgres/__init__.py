import os

from src.models.postgres.base_model import get_pg_session, set_session, Base
from src.models.postgres.images_info_model import ImagesInfoModel, ImagesInfoSchema
from src.models.postgres.rule34_images_info import Rule34ImagesInfoModel, Rule34ImagesInfoSchema

set_session()
