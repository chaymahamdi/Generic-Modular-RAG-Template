from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict


class BaseSchema(BaseModel):
    id: str | None = Field(default=None, description="The primary key")
    creation_date: datetime = Field(default=None, description="The creation date")
    deleted: bool = Field(default=False, description="Whether the record is deleted")

    model_config = ConfigDict(from_attributes=True)

class DocumentBase(BaseSchema):
    title: str | None= Field(default=None, description="The title of the document")
    size: str | None= Field(default=None, description="The size of the document")
    content: str | None= Field(default=None, description="The content of the document")

