from dependency_injector.wiring import Provide,inject
from fastapi import APIRouter, Depends

from configuration.di_container import ServiceDIContainer
from src.schemas.service_schemas import DocumentBase
from src.services.document_service import DocumentService

document_router = APIRouter(prefix="/document")

from uuid import UUID


@document_router.get("/documents/{document_id}", response_model=DocumentBase)
@inject
def get_document(document_id: UUID,
                 document_service: DocumentService= Depends(Provide[ServiceDIContainer.document_service])) -> DocumentBase:
    return document_service.get_document_by_id(document_id)