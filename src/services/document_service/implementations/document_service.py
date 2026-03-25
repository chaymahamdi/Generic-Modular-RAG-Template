from uuid import UUID

from fastapi import UploadFile
from pydantic import ValidationError

from configuration.logging_configuration import logger
from src.execptions.repository_exceptions import DocumentNotFound, DatabaseConnectionError
from src.execptions.service_exceptions import SchemaMappingException
from src.repositories.document_repository import DocumentRepository
from src.schemas.service_schemas import DocumentBase, FileFormat, DocumentCreate
from src.services.document_service.document_parsers.parser_factory import ParserFactory
from src.services.document_service.interfaces.document_interface import IDocumentService
from src.utils.document_parser_utils import detect_language, get_document_extension


class DocumentService(IDocumentService):

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


    async def parse_document(self, document: UploadFile) -> DocumentBase:
        """
          Parse an uploaded document and store it in the database.

          This method reads the file content, selects the appropriate parser based on the file format,
          extracts the textual content, detects the document language, and persists the result.

          :param document: Uploaded file to be processed.
          :return: DocumentBase containing parsed content, metadata, and detected language.
        """
        document_content = await document.read()

        filename = document.filename
        document_extension = get_document_extension(filename)
        document_size = str(document.size)

        parser = ParserFactory.get_parser(document_extension)

        parsed_content = parser.parse_document(document_content)
        detected_language = detect_language(parsed_content.content)
        parsed_document = DocumentCreate(content=parsed_content.content,language=detected_language,title=filename,
                                       size=document_size,source=FileFormat(document_extension).value)

        created_document = self.document_repository.create_document(parsed_document)

        logger.info(f"Created Document {created_document.id}")
        result= DocumentBase.model_validate(created_document)
        return result


