from uuid import UUID

from sqlalchemy.exc import SQLAlchemyError

from configuration.logging_configuration import logger
from src.execptions.repository_exceptions import DatabaseConnectionError, DocumentNotFound
from src.models.db_helper import DBHelper
from src.models.document_table import Document
from src.schemas.service_schemas import DocumentBase, DocumentCreate


class DocumentRepository:

    def __init__(self, db_helper: DBHelper):
        """initiate the document repository with vector database helper"""
        self.db_helper = db_helper

    def get_document_by_id(self, document_id: UUID) -> Document:
        """
         get the document by id in repository layer
            :param document_id: UUID of the document
            :return Document ORM object
        """
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

    def create_document(self, document_data: DocumentCreate) -> Document:
        """
        Create a new document in the repository layer.

        :param document_data: DocumentBase schema containing document fields
        :return: Created Document ORM object
        """
        try:
            with self.db_helper.session() as session:
                new_document = Document(**document_data.model_dump())
                session.add(new_document)
                session.commit()
                session.refresh(new_document)
                logger.info(f"Document {new_document.id} was created successfully")
                return new_document

        except SQLAlchemyError as e:
            logger.error(e)
            raise DatabaseConnectionError() from e

