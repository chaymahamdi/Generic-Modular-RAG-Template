from datetime import datetime
from uuid import uuid4

from sqlalchemy import Boolean, DateTime, UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapped_column, Mapped

Base = declarative_base()

class BaseTable(Base):
    __abstract__ = True
    id : Mapped[UUID] =  mapped_column(UUID, primary_key=True, default=uuid4, unique=True)
    creation_date : Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now, nullable=False)
    deleted : Mapped[bool] = mapped_column(Boolean, default=False)