from enum import Enum


class ModelProvider(str, Enum):
    OLLAMA = "ollama"


class ModelType(str, Enum):
    EMBEDDING = "embedding"
    CHAT = "chat"
