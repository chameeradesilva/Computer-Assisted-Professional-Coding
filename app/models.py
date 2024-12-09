from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class ClinicalDocument(Base):
    __tablename__ = "clinical_documents"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class SuggestedCode(Base):
    __tablename__ = "suggested_codes"
    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer, ForeignKey("clinical_documents.id"))
    code_type = Column(String, nullable=False)  # ICD-10 or CPT
    code = Column(String, nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
