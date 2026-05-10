from abc import ABC, abstractmethod
from typing import Sequence

class IEmbeddingModel(ABC):

    @abstractmethod
    async def embed_text(self, model_name: str, text: str) -> Sequence[float]:
        """
        Generate an embedding vector for a single text input.
         :param model_name: Name of the model to use for embedding
        :param text: Input text to embed
        :return: List of floats representing the embedding vector
        """
        pass

    @abstractmethod
    async def embed_batch(self, model_name: str, texts: list[str]) -> Sequence[Sequence[float]]:

        """
        Generate embedding vectors for a batch of text inputs.
        :param model_name: Name of the model to use for embedding
        :param texts: List of input texts to embed
        :return: List of embedding vectors
        """
        pass
