from fastapi import Request
from fastapi.responses import JSONResponse

from src.execptions.repository_exceptions import DatabaseConnectionError, DocumentNotFound
from src.execptions.service_exceptions import SchemaMappingException


def register_exception_handlers(app):

    @app.exception_handler(DocumentNotFound)
    async def document_not_found_handler(request:Request, exc: DocumentNotFound):
        return JSONResponse(
            status_code=404,
            content={"detail": str(exc)},
        )

    @app.exception_handler(DatabaseConnectionError)
    async def database_exception_handler(request:Request, exc: DatabaseConnectionError):
        return JSONResponse(
            status_code=500,
            content={"detail": "Database connection error"},
        )

    @app.exception_handler(SchemaMappingException)
    async def mapping_exception_handler(request:Request, exc: SchemaMappingException):
        return JSONResponse(
            status_code=500,
            content={"detail": "Data mapping error"},
        )