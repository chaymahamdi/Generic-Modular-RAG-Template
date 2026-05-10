from abc import ABC,abstractmethod
from io import BytesIO
from uuid import UUID

from fastapi import UploadFile

from src.schemas.service_schemas import DocumentBase


class IDocumentService(ABC):

    @abstractmethod
    async def get_document_by_id(self, document_id: UUID) -> DocumentBase:
        """
         get document data by id
        :param document_id: uuid of document
        :return DocumentBase document details
        """
        pass

    @abstractmethod
    async def parse_document(self, document:UploadFile) -> DocumentBase:
        """
         ingest uploaded file in database by type
        :param document : BytesIO with file data
        :return DocumentBase document details
        """
        pass
