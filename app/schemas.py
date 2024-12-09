from pydantic import BaseModel

class ClinicalDocumentCreate(BaseModel):
    title: str
    content: str

class SuggestedCodeResponse(BaseModel):
    code_type: str
    code: str
    description: str
