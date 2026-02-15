from fastapi import FastAPI
from uvicorn import Server, Config

from configuration.app_settings import AppSettings
from configuration.logging_configuration import logging_config
from middlewares.app_middlewares import middlewares

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


if __name__ == '__main__':
    Server(Config(
        app=app,
        host=app_settings.HOST,
        port=app_settings.PORT,
        log_config=logging_config,
        workers=app_settings.NB_WORKERS
    )).run()
