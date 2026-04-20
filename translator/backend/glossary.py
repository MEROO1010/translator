from typing import Dict, Optional
import json
import os

class GlossaryManager:
    def __init__(self, user_id: str, storage_dir: str = "glossaries"):
        self.user_id = user_id
        self.storage_dir = storage_dir
        os.makedirs(storage_dir, exist_ok=True)

    def load_glossary(self) -> Dict[str, str]:
        try:
            with open(f"{self.storage_dir}/{self.user_id}.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save_glossary(self, glossary: Dict[str, str]) -> None:
        with open(f"{self.storage_dir}/{self.user_id}.json", "w") as f:
            json.dump(glossary, f)

    def add_term(self, source: str, target: str) -> None:
        glossary = self.load_glossary()
        glossary[source] = target
        self.save_glossary(glossary)