import datetime
from typing import List

from pydantic import Field, BaseModel as BaseSchema


class PayloadSchema(BaseSchema):
    id: int
    author: str
    image_title: str
    image_tags: List[str]
    image_description: str
    image_path: str
    image_url: str
    published_at: datetime.datetime = Field(default_factory=datetime.datetime.now())
    inserted_at: datetime.datetime = Field(default_factory=datetime.datetime.now())
