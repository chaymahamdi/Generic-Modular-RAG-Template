from fastapi import FastAPI
from uvicorn import Server, Config

from configuration.app_settings import AppSettings
from configuration.di_container import ServiceDIContainer
from configuration.logging_configuration import logging_config
from middlewares.app_middlewares import middlewares
from src.apis.document_api import document_router
from src.apis.exception_handlers import register_exception_handlers

app_settings = AppSettings()

def get_application() -> FastAPI:
    application = FastAPI(
        title=app_settings.PROJECT_NAME, openapi_url="/docs/swagger.json",
        description="Swagger for general purpose RAG-System + PGVector",
        docs_url="/docs",
        redoc_url="/redocs",
        middlewares=middlewares
    )

    return application

app = get_application()
register_exception_handlers(app)

app.container = ServiceDIContainer()

app.include_router(document_router, tags=["document_api"])

if __name__ == '__main__':
    Server(Config(
        app=app,
        host=app_settings.HOST,
        port=app_settings.PORT,
        log_config=logging_config,
        workers=app_settings.NB_WORKERS
    )).run()
