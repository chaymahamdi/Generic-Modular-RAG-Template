from abc import ABC, abstractmethod
from io import BytesIO

from src.schemas.service_schemas import ParsedDocument


class BaseParser(ABC):

    @abstractmethod
    def parse_document(self, document: bytes) -> ParsedDocument:
        """
         interface for document parsers based on the format(PDF,WORD,XLSX)
        :param document: bytesIO
        :return uploaded document details
        """
        pass
