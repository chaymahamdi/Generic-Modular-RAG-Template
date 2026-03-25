from typing import Type, Any

from src.services.document_service.document_parsers.base_parser import BaseParser
from src.services.document_service.document_parsers.pdf_parser_implementation import PDFParser

class ParserFactory:

    _parsers: dict[str, Type[BaseParser]] = {
        "pdf": PDFParser,
    }

    @classmethod
    def get_parser(cls, extension: str) -> BaseParser:
        parser_class = cls._parsers.get(extension.lower())

        if not parser_class:
            raise ValueError(f"We couldn't parse this document, this extension {extension} is not supported yet !")

        return parser_class()