from pydantic import BaseModel
from typing import Dict, Optional

class TranslationRequest(BaseModel):
    text: str
    target_lang: str
    context_type: Optional[str] = None
    glossary: Optional[Dict[str, str]] = {}
    api_keys: Dict[str, str]  # {"openai": "...", "deepl": "...", "google": "..."}

class TranslationResult(BaseModel):
    engine: str
    source_text: str
    translated_text: str
    target_lang: str

class TranslationError(Exception):
    pass