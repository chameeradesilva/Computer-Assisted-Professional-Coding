import spacy

nlp = spacy.load("en_core_web_sm")  # Replace with a domain-specific model if needed.

def extract_entities(text: str):
    doc = nlp(text)
    entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
    return entities
