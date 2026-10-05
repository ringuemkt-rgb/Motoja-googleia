from typing import Any
import httpx
from .config import settings

class LLMUnavailable(RuntimeError):
    pass

class CompatibleChatClient:
    """Adapter for a generic chat-completions compatible endpoint."""

    def __init__(self):
        self.base_url = settings.llm_base_url
        self.api_key = settings.llm_api_key
        self.model = settings.llm_model

    @property
    def configured(self) -> bool:
        return bool(self.base_url and self.model)

    async def complete(self, system: str, user: str, temperature: float = 0.1) -> str:
        if not self.configured:
            raise LLMUnavailable("No LLM endpoint configured")
        headers = {"Content-Type":"application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        payload: dict[str, Any] = {
            "model": self.model,
            "temperature": temperature,
            "messages": [
                {"role":"system","content":system},
                {"role":"user","content":user},
            ],
        }
        async with httpx.AsyncClient(timeout=90) as client:
            response = await client.post(
                self.base_url.rstrip("/") + "/v1/chat/completions",
                headers=headers, json=payload
            )
            response.raise_for_status()
            data = response.json()
        return data["choices"][0]["message"]["content"]
