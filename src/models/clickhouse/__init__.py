import os

from src.models.clickhouse.base_model import get_pg_session
from src.models.clickhouse.images_info_model import ImagesInfoModel, ImagesInfoSchema

# if "TEST_CASE" not in os.environ:
#     set_ch_session()
