import datetime

from pydantic import Field, BaseModel as BaseSchema
from sqlalchemy import Column
from clickhouse_sqlalchemy.types import UInt64, String, DateTime
from clickhouse_sqlalchemy import engines

from src.models.clickhouse.base_model import Base


class ImagesInfoModel(Base):
    __tablename__ = 'images_info'

    id = Column("id", UInt64, primary_key=True)
    image_description = Column("image_description", String, default="")
    image_path = Column("image_path", String, default="")
    image_url = Column("image_url", String, default="")
    inserted_at = Column("inserted_at", DateTime, )

    __table_args__ = (
        engines.Memory(),
    )


class ImagesInfoSchema(BaseSchema):
    id: int
    image_description: str
    image_path: str
    image_url: str
    inserted_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
