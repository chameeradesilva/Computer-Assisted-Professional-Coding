from fastapi import APIRouter, HTTPException
from app.utils.nlp_utils import extract_entities

router = APIRouter()

@router.post("/extract")
def extract_information(document: dict):
    content = document.get("content")
    if not content:
        raise HTTPException(status_code=400, detail="Content is required")
    entities = extract_entities(content)
    return {"entities": entities}
