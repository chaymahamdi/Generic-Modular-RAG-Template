from datetime import datetime
from enum import Enum
from uuid import UUID

from pydantic import BaseModel, Field, ConfigDict


class FileFormat(str, Enum):
    PDF = "pdf"
    DOCX = "docx"
    XLSX = "xlsx"
    TXT = "txt"

class BaseSchema(BaseModel):
    id: UUID | None = Field(default=None, description="The primary key")
    creation_date: datetime = Field(default=None, description="The creation date")
    deleted: bool = Field(default=False, description="Whether the record is deleted")

    model_config = ConfigDict(from_attributes=True)

class ParsedDocument(BaseModel):
    content: str | None= Field(default=None, description="The content of the document")

class DocumentCreate(ParsedDocument):
    title: str | None = Field(default=None, description="The title/filename of the document")
    size: str | None = Field(default=None, description="The size of the document")
    source: str | None = Field(default=None, description="The type of the document")
    language: str | None = Field(default=None, description="The type of the document")

class DocumentBase(BaseSchema, ParsedDocument):
    title: str | None = Field(default=None, description="The title/filename of the document")
    size: str | None = Field(default=None, description="The size of the document")
    source: FileFormat | None = Field(default=None, description="The type of the document")
    language: str | None = Field(default=None, description="The language of the document")