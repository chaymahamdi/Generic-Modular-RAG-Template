from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, Boolean, DateTime, UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseTable(Base):
    __abstract__ = True
    id = Column(UUID, primary_key=True, default=uuid4, unique=True)
    creation_date = Column(DateTime(timezone=True), default=datetime.now, nullable=False)
    deleted = Column(Boolean, default=False)