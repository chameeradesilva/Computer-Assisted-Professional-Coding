from fastapi import APIRouter, HTTPException
from app.utils.coding_utils import suggest_codes
from app.schemas import SuggestedCodeResponse

router = APIRouter()

@router.post("/suggest", response_model=list[SuggestedCodeResponse])
def suggest_coding(document: dict):
    content = document.get("content")
    if not content:
        raise HTTPException(status_code=400, detail="Content is required")
    codes = suggest_codes(content)
    return codes
