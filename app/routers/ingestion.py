from fastapi import APIRouter, HTTPException
from app.schemas import ClinicalDocumentCreate
from app.models import ClinicalDocument
from app.database import SessionLocal

router = APIRouter()

@router.post("/")
def ingest_document(doc: ClinicalDocumentCreate):
    db = SessionLocal()
    new_doc = ClinicalDocument(title=doc.title, content=doc.content)
    db.add(new_doc)
    db.commit()
    db.refresh(new_doc)
    db.close()
    return {"message": "Document ingested successfully", "document_id": new_doc.id}
