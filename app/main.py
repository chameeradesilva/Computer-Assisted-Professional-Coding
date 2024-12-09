from fastapi import FastAPI
# from app.routers import ingestion, nlp, coding

app = FastAPI(
    title="Computer-Assisted Professional Coding for RCM",
    description="Automated ICD-10 and CPT coding with claims submission.",
    version="1.0.0"
)

# Registering Routers
app.include_router(ingestion.router, prefix="/api/ingestion", tags=["Ingestion"])
app.include_router(nlp.router, prefix="/api/nlp", tags=["NLP"])
app.include_router(coding.router, prefix="/api/coding", tags=["Coding"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the CAPC API!"}
