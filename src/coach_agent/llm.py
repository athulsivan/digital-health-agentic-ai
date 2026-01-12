import requests
from .config import settings

def generate(prompt: str, timeout_s: int = 120) -> str:
    """
    Generate text using Ollama's local HTTP API.
    Keeps the interface tiny so the rest of the system stays model-agnostic.
    """
    if settings.model_backend != "ollama":
        raise ValueError(f"Unsupported MODEL_BACKEND={settings.model_backend}")

    url = f"{settings.ollama_host}/api/generate"
    payload = {
        "model": settings.ollama_model,
        "prompt": prompt,
        "stream": False,
    }

    r = requests.post(url, json=payload, timeout=timeout_s)
    r.raise_for_status()
    data = r.json()
    return data.get("response", "").strip()
