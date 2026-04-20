import deepl
from typing import Optional, Dict
from .models import TranslationResult, TranslationError

class DeepLTranslator:
    def __init__(self, api_key: str):
        self.translator = deepl.Translator(api_key)

    def translate(
        self,
        text: str,
        target_lang: str,
        context: Optional[str] = None,
        glossary: Optional[Dict[str, str]] = None,
    ) -> TranslationResult:
        try:
            result = self.translator.translate_text(
                text,
                target_lang=target_lang,
                context=context,
                glossary=glossary,
            )
            return TranslationResult(
                engine="deepl",
                source_text=text,
                translated_text=result.text,
                target_lang=target_lang,
            )
        except Exception as e:
            raise TranslationError(f"DeepL translation failed: {str(e)}")