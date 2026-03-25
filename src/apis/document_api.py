import json
from http import HTTPStatus

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, UploadFile, File
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from configuration.di_container import ServiceDIContainer
from src.schemas.service_schemas import DocumentBase
from src.services.document_service.implementations.document_service import DocumentService

document_router = APIRouter(prefix="/document")

from uuid import UUID


@document_router.post("/ingest",description="Ingest files")
@inject
async def ingest_document(uploaded_file: UploadFile = File(...),
                 document_service: DocumentService= Depends(Provide[ServiceDIContainer.document_service])) -> JSONResponse:

    parsed_document= await document_service.parse_document(uploaded_file)
    return JSONResponse(status_code=HTTPStatus.OK, content=jsonable_encoder(parsed_document))

@document_router.get("/{document_id}", response_model=DocumentBase)
@inject
def get_document(document_id: UUID,
                 document_service: DocumentService= Depends(Provide[ServiceDIContainer.document_service])) -> DocumentBase:
    return document_service.get_document_by_id(document_id)