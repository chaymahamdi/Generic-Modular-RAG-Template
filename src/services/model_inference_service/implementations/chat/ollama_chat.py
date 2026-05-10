from typing import AsyncGenerator

from ollama import AsyncClient

from configuration.logging_configuration import logger
from src.services.model_inference_service.interfaces.chat_model_interface import IChatModel


class OllamaChatModel(IChatModel):

    def __init__(self, base_url: str, model_name: str):
        self.client = AsyncClient(host=base_url)
        self.model_name = model_name

    async def generate(self, prompt: str, **kwargs) -> str | None:
        """Generate a response from chatOllama.
        :param prompt: Input prompt
        :param kwargs: Additional keyword arguments
        :return: Generated response
        """
        response = await self.client.chat(
            model=self.model_name,
            messages=[{"role": "user", "content": prompt}],
            options=kwargs.get('temperature', 1),
            stream=False,
            **kwargs,
        )
        logger.info(f"Generated response with model {self.model_name}")
        return response.message.content

    async def generate_stream(self, prompt: str, **kwargs) -> AsyncGenerator[str, None]:
        """Stream response tokens from chatOllama.
        :param prompt: Input prompt
        :param kwargs: Additional keyword arguments
        :return: Async generator of response tokens
        """
        stream = await self.client.chat(
            model=self.model_name,
            messages=[{"role": "user", "content": prompt}],
            stream=True,
            **kwargs,
        )
        async for chunk in stream:
            content = chunk.message.content
            if content:
                yield content
