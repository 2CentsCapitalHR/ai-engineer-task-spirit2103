import json
from docx import Document
import io

with open("checklist_mapping.json", "r") as f:
    CHECKLISTS = json.load(f)

KEYWORDS = {
    "Articles of Association": ["articles of association", "aoa", "articles"],
    "Memorandum of Association": ["memorandum of association", "moa", "memorandum"],
    "Incorporation Application Form": ["incorporation application", "application form"],
    "UBO Declaration Form": ["ubo declaration", "ultimate beneficial owner"],
    "Register of Members and Directors": ["register of members", "register of directors"]
}

def simple_keyword_detect(docx_bytes: bytes) -> str:
    doc = Document(io.BytesIO(docx_bytes))
    text = "\n".join([p.text for p in doc.paragraphs]).lower()
    for label, kwlist in KEYWORDS.items():
        if any(kw in text for kw in kwlist):
            return label
    return "Unknown Document Type"

def compare_against_checklist(process: str, uploaded_types: list):
    required = CHECKLISTS.get(process, [])
    missing = [r for r in required if r not in uploaded_types]
    return {
        "process": process,
        "required_documents": required,
        "uploaded_documents": uploaded_types,
        "missing_documents": missing
    }
