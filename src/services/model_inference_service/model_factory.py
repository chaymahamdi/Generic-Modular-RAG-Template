from typing import Type

from src.services.model_inference_service.implementations.chat.ollama_chat import OllamaChatModel
from src.services.model_inference_service.implementations.embedding.ollama_embedding import OllamaEmbeddingModel
from src.services.model_inference_service.interfaces.chat_model_interface import IChatModel
from src.services.model_inference_service.interfaces.embedding_model_interface import IEmbeddingModel
from src.services.model_inference_service.model_enums import ModelProvider


class ModelFactory:
    """
    Factory to resolve model implementations by provider.
    To add a new provider:
      1. Create a new implementation under implementations/embedding/ or implementations/chat/
      2. Register it in the corresponding dict below.
    """

    _embedding_providers: dict[ModelProvider, Type[IEmbeddingModel]] = {
        ModelProvider.OLLAMA: OllamaEmbeddingModel,
    }

    _chat_providers: dict[ModelProvider, Type[IChatModel]] = {
        ModelProvider.OLLAMA: OllamaChatModel,
    }

    @classmethod
    def get_embedding_model(cls, provider: ModelProvider, base_url: str, model_name: str) -> IEmbeddingModel:
        model_class = cls._embedding_providers.get(provider)
        if not model_class:
            raise ValueError(f"Embedding provider '{provider.value}' is not supported yet!")
        return model_class(base_url=base_url, model_name=model_name)

    @classmethod
    def get_chat_model(cls, provider: ModelProvider, base_url: str, model_name: str) -> IChatModel:
        model_class = cls._chat_providers.get(provider)
        if not model_class:
            raise ValueError(f"Chat provider '{provider.value}' is not supported yet!")
        return model_class(base_url=base_url, model_name=model_name)
