from uuid import UUID

from pydantic import ValidationError

from configuration.logging_configuration import logger
from src.execptions.repository_exceptions import DocumentNotFound, DatabaseConnectionError
from src.execptions.service_exceptions import SchemaMappingException
from src.repositories.document_repository import DocumentRepository
from src.schemas.service_schemas import DocumentBase


class DocumentService:

    def __init__(self, document_repository: DocumentRepository):
        self.document_repository = document_repository

    def get_document_by_id(self, document_id: UUID) -> DocumentBase:
        """get ingested document details by ID"""
        try:
            result=self.document_repository.get_document_by_id(document_id)
            return DocumentBase.model_validate(result)
        except (DocumentNotFound,DatabaseConnectionError):
            raise
        except ValidationError as e:
            logger.error(f"Error to map Document ID {document_id} to DocumentBase {e}")
            raise SchemaMappingException(f"Error while mapping Document {document_id} to schema") from e




