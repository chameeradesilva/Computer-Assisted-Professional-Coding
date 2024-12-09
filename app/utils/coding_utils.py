def suggest_codes(text: str):
    # Mock logic for ICD-10 and CPT codes
    icd_codes = [{"code_type": "ICD-10", "code": "E11.9", "description": "Type 2 diabetes mellitus"}]
    cpt_codes = [{"code_type": "CPT", "code": "99213", "description": "Office visit, established patient"}]
    return icd_codes + cpt_codes
