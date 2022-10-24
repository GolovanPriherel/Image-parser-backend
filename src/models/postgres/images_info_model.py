import datetime
from typing import List

from pydantic import Field, PositiveInt, BaseModel as BaseSchema
from sqlalchemy import Column
from sqlalchemy.types import Integer, String, DateTime, ARRAY

from src.models.postgres.base_model import Base


class ImagesInfoModel(Base):
    __tablename__ = "images_info"

    id = Column("id", Integer, primary_key=True)
    image_title = Column("image_title", String, default="")
    image_tags = Column("image_tags", ARRAY(String), default=[""])
    image_description = Column("image_description", String, default="")
    image_path = Column("image_path", String, default="")
    image_url = Column("image_url", String, default="")
    inserted_at = Column("inserted_at", DateTime, default=str(datetime.datetime.now()))

    __table_args__ = {'extend_existing': True}


class ImagesInfoSchema(BaseSchema):
    id: PositiveInt = Field(default_factory=1)
    image_title: str = Field(default_factory="")
    image_tags: List[str] = Field(default_factory=[""])
    image_description: str = Field(default_factory="")
    image_path: str = Field(default_factory="")
    image_url: str = Field(default_factory="")
    inserted_at: datetime.datetime = Field(default_factory=datetime.datetime.now())
