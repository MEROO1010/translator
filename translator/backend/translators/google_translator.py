from googletrans import Translator
from typing import Optional, Dict
from .models import TranslationResult, TranslationError

class GoogleTranslator:
    def __init__(self):
        self.translator = Translator()

    def translate(
        self,
        text: str,
        target_lang: str,
        context: Optional[str] = None,
        glossary: Optional[Dict[str, str]] = None,
    ) -> TranslationResult:
        try:
            result = self.translator.translate(text, dest=target_lang)
            return TranslationResult(
                engine="google",
                source_text=text,
                translated_text=result.text,
                target_lang=target_lang,
            )
        except Exception as e:
            raise TranslationError(f"Google translation failed: {str(e)}")