from abc import ABC, abstractmethod
from typing import AsyncGenerator


class IChatModel(ABC):

    @abstractmethod
    async def generate(self, prompt: str, **kwargs) -> str:
        """
        Generate a response for a given prompt.
        :param prompt: User prompt / input text
        :return: Generated response string
        """
        pass

    @abstractmethod
    async def generate_stream(self, prompt: str, **kwargs) -> AsyncGenerator[str, None]:
        """
        Stream a response token by token for a given prompt.
        :param prompt: User prompt / input text
        :return: Async generator yielding response chunks
        """
        pass
