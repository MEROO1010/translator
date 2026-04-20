from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from .translators import OpenAITranslator, DeepLTranslator, GoogleTranslator
from .context_manager import get_context_template
from .glossary import GlossaryManager
from .batch_processor import BatchProcessor
from .models import TranslationRequest, TranslationResult

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"])

@app.post("/translate")
async def translate(request: TranslationRequest):
    results = {}
    for engine in ["openai", "deepl", "google"]:
        translator = globals()[f"{engine.capitalize()}Translator"](api_key=request.api_keys[engine])
        context = get_context_template(request.context_type) if request.context_type else None
        result = translator.translate(
            text=request.text,
            target_lang=request.target_lang,
            context=context,
            glossary=request.glossary,
        )
        results[engine] = result
    return {"results": results}

@app.post("/batch")
async def batch_translate(
    file: UploadFile = File(...),
    source_col: str = "text",
    target_lang: str = "ar",
):
    processor = BatchProcessor(**request.api_keys)
    processor.process_csv(file.filename, source_col, target_lang, "output.csv")
    return {"status": "success"}