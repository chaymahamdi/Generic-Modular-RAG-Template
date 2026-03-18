from sqlalchemy import Column, String

from src.models.common_models import BaseTable

class DocumentTable(BaseTable):
    __tablename__ = 'documents'
    title=Column(String(255), nullable=False)
    size=Column(String(50))
    content= Column(String)