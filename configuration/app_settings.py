from pydantic import Field
from pydantic_settings import BaseSettings

class AppSettings(BaseSettings):
    LOG_LEVEL: str = Field(default="INFO", alias="LOG_LEVEL")
    HOST: str = Field(alias="APP_HOST", default="localhost")
    PORT: int = Field(alias="APP_PORT", default="8008")
    API_VERSION: str = Field(default="v1", alias="API_VERSION")
    PROJECT_NAME: str = Field(alias="PROJECT_NAME", default="General-Purpose-RAG-System")
    NB_WORKERS: int = Field(alias="NB_WORKERS", default=3)

class VectorDatabaseConfig(BaseSettings):
    """Configuration class for connecting to the PGVector as vector database"""
    VECTOR_DB_HOST: str = Field(alias='VECTOR_DB_HOST', default='0.0.0.0', description="Host for running the vector database :pgvector")
    VECTOR_DB_PORT: int = Field(alias='VECTOR_DB_PORT', default=5435, description="Port for running the vector database :pgvector")
    VECTOR_DB_NAME: str = Field(alias='VECTOR_DB_NAME', default='rag_system_vector_db', description="Vector Database name")
    VECTOR_DB_USER: str = Field(alias='VECTOR_DB_USER', default='rag_system_username', description="Username to access the vector database")
    VECTOR_DB_PASSWORD: str = Field(alias='VECTOR_DB_PASSWORD', default='rag_system_password', description="password to access the vector database")

    @property
    def db_url(self):
        return f"postgresql+psycopg://{self.VECTOR_DB_HOST}:{self.VECTOR_DB_PORT}/{self.VECTOR_DB_NAME}?user={self.VECTOR_DB_USER}&password={self.VECTOR_DB_PASSWORD}"