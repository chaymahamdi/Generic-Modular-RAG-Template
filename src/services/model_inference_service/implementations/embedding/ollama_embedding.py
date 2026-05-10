from typing import Sequence

from ollama import AsyncClient

from configuration.logging_configuration import logger
from src.services.model_inference_service.interfaces.embedding_model_interface import IEmbeddingModel


class OllamaEmbeddingModel(IEmbeddingModel):

    def __init__(self, base_url: str):
        self.client = AsyncClient(host=base_url)

    async def embed_text(self, model_name: str, text: str) -> Sequence[float]:
        """Generate embedding for an input text
        :param model_name: name of the model to use
        :param text: input text
        :return: list of floats representing the embedding
        """
        response = await self.client.embed(model=model_name, input=text)
        logger.info(f"Generated embedding with model {model_name}")
        return response.embeddings[0]

    async def embed_batch(self, model_name: str, texts: list[str]) -> Sequence[Sequence[float]]:
        """Generate embeddings for a batch of texts
        :param model_name: the embedding model to use
        :param texts: list of texts to generate embeddings for
        :return: list of lists of floats representing the embeddings
        """
        response = await self.client.embed(model=model_name, input=texts)
        logger.info(f"Generated {len(texts)} embeddings with model {model_name}")
        return response.embeddings
