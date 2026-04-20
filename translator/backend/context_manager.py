CONTEXT_TEMPLATES = {
    "technical": "Translate as a technical document with precise terminology.",
    "legal": "Translate as a legal document, preserving formal language.",
    "medical": "Translate as a medical text, ensuring accuracy of terms.",
    "literary": "Translate as a literary work, preserving style and tone.",
}

def get_context_template(context_type: str) -> str:
    return CONTEXT_TEMPLATES.get(context_type, "")