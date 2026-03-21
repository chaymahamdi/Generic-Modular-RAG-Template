from uuid import UUID

from sqlalchemy.exc import SQLAlchemyError

from configuration.logging_configuration import logger
from src.execptions.repository_exceptions import DatabaseConnectionError, DocumentNotFound
from src.models.db_helper import DBHelper
from src.models.document_table import Document


class DocumentRepository:

    def __init__(self, db_helper: DBHelper):
        """initiate the document repository with vector database helper"""
        self.db_helper = db_helper

    def get_document_by_id(self, document_id: UUID) -> Document:
        try:
            with self.db_helper.session() as session:
                document = (
                    session.query(Document)
                    .filter(Document.id == document_id)
                    .one_or_none()
                )

                if not document:
                    raise DocumentNotFound(document_id)
                logger.info(f"Document {document_id} was found successfully")
                return document

        except SQLAlchemyError as e:
            logger.error(e)
            raise DatabaseConnectionError() from e
