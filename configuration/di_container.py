from dependency_injector import containers, providers

from configuration.app_settings import AppSettings,VectorDatabaseConfig
from src.models.db_helper import DBHelper
from src.repositories.document_repository import DocumentRepository
from src.services.document_service.implementations.document_service import DocumentService


class ServiceDIContainer(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(packages=["src"])

    app_settings= providers.Singleton(AppSettings)
    vector_database_config= providers.Singleton(VectorDatabaseConfig)

    vector_db_helpers = providers.Singleton(
        DBHelper, db_url=vector_database_config.provided.db_url)

    document_repository= providers.Singleton(DocumentRepository,db_helper=vector_db_helpers)

    document_service= providers.Singleton(DocumentService,document_repository=document_repository)