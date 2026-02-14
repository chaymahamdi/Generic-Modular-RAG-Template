from pydantic import Field
from pydantic_settings import BaseSettings

class AppSettings(BaseSettings):
    LOG_LEVEL: str = Field(default="INFO", alias="LOG_LEVEL")
    HOST: str = Field(alias="APP_HOST", default="localhost")
    PORT: int = Field(alias="APP_PORT", default="8008")
    API_VERSION: str = Field(default="v1", alias="API_VERSION")
    PROJECT_NAME: str = Field(alias="PROJECT_NAME", default="General-Purpose-RAG-System")
    NB_WORKERS: int = Field(alias="NB_WORKERS", default=3)