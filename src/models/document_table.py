from sqlalchemy import String
from sqlalchemy.orm import Mapped, relationship, mapped_column

from src.models.common_models import BaseTable


class Document(BaseTable):
    __tablename__ = 'document'
    title: Mapped[str]= mapped_column(String(255), nullable=False)
    size: Mapped[str]= mapped_column(String(50))
    content: Mapped[str]= mapped_column(String)
    source: Mapped[str]= mapped_column(String(20))
    language: Mapped[str]= mapped_column(String(10))
    chunks: Mapped[list["DocumentChunk"]]= relationship(back_populates="document", cascade="all, delete-orphan")