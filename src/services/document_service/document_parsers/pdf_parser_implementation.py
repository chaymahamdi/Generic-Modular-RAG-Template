
import pymupdf
from pymupdf4llm import to_markdown

from src.schemas.service_schemas import ParsedDocument
from src.services.document_service.document_parsers.base_parser import BaseParser


class PDFParser(BaseParser):

    def parse_document(self, document:bytes) -> ParsedDocument:
        """
         parse the PDF file using pymupdf4llm to parse the document into structured sections
        :param document: BytesIO containing the PDF file
        :return
        """
        doc = pymupdf.open(stream=document, filetype="pdf")
        markdown_parsed_text= to_markdown(doc,use_ocr=False,ignore_images=True)
        return ParsedDocument(content=markdown_parsed_text)


