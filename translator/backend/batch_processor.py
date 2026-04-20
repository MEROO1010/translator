import pandas as pd
from typing import List
from .translators import OpenAITranslator, DeepLTranslator, GoogleTranslator

class BatchProcessor:
    def __init__(self, openai_key: str, deepl_key: str, google_key: str):
        self.translators = {
            "openai": OpenAITranslator(openai_key),
            "deepl": DeepLTranslator(deepl_key),
            "google": GoogleTranslator(google_key),
        }

    def process_csv(
        self,
        file_path: str,
        source_col: str,
        target_lang: str,
        output_path: str,
    ) -> None:
        df = pd.read_csv(file_path)
        for engine in self.translators:
            df[f"{source_col}_{engine}"] = df[source_col].apply(
                lambda x: self.translators[engine].translate(x, target_lang).translated_text
            )
        df.to_csv(output_path, index=False)