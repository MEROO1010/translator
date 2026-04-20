import openai
from typing import Optional, Dict
from ..models import TranslationResult

class OpenAITranslator:
    def __init__(self, api_key: str):
        self.api_key = api_key
        openai.api_key = api_key

    def translate(
        self,
        text: str,
        target_lang: str,
        context: Optional[str] = None,
        glossary: Optional[Dict[str, str]] = None,
    ) -> TranslationResult:
        try:
            prompt = f"Translate to {target_lang}: {text}"
            if context:
                prompt += f"\nContext: {context}"
            if glossary:
                prompt += f"\nGlossary: {glossary}"

            response = openai.ChatCompletion.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}],
            )
            translation = response.choices[0].message["content"].strip()

            return TranslationResult(
                engine="openai",
                source_text=text,
                translated_text=translation,
                target_lang=target_lang,
            )
        except Exception as e:
            raise TranslationError(f"OpenAI translation failed: {str(e)}")