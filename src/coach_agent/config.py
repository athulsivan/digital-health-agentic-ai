from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()  # loads .env if present

class Settings(BaseModel):
    model_backend: str = os.getenv("MODEL_BACKEND", "ollama")
    ollama_host: str = os.getenv("OLLAMA_HOST", "http://localhost:11434")
    ollama_model: str = os.getenv("OLLAMA_MODEL", "llama3.1:8b")

settings = Settings()

