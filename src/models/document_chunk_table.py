from uuid import UUID

from pgvector.sqlalchemy import Vector
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.models.common_models import BaseTable


class DocumentChunk(BaseTable):
    __tablename__ = 'document_chunk'
    content : Mapped[str] = mapped_column(String, nullable=False)
    embedding : Mapped[list[float]] =  mapped_column(Vector(768))
    document_id : Mapped[UUID] = mapped_column(ForeignKey('document.id'), nullable=False)
    document: Mapped["Document"] = relationship(back_populates="chunks")
