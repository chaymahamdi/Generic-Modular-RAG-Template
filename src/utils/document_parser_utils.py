import os

from langdetect import detect, LangDetectException

from configuration.logging_configuration import logger


def detect_language(text:str) -> str| None:
    """
     detects the language of the given text using langdetect.
    :param text:
    :return:
    """
    try:
        if text.strip() != "":
            return detect(text)
    except LangDetectException:
        logger.error("Could not detect language using langdetect.")
    return None

def get_document_extension(path:str) -> str| None:
    """
     gets the extension of the given path
    :param path: str of path
    :return the extension of the given path ( PDF, DOCX,...)
    """
    _,extension= os.path.splitext(path)
    return extension.lower()[1:] if extension and len(extension) > 1 else None