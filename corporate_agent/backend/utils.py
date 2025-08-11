import json
from langchain_huggingface import HuggingFaceEmbeddings

# Load checklist mapping
with open("checklist_mapping.json", "r") as f:
    CHECKLISTS = json.load(f)

# Load embeddings model once
embeddings_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def compare_against_checklist(process: str, uploaded_types: list, similarity_threshold=0.75):
    """
    Compare uploaded document types against required documents using embeddings.
    Returns missing documents even if names are slightly different.
    """
    required_docs = CHECKLISTS.get(process, [])
    missing_docs = []

    for req_doc in required_docs:
        matched = False
        req_emb = embeddings_model.embed_query(req_doc)
        for uploaded in uploaded_types:
            up_emb = embeddings_model.embed_query(uploaded)
            sim = cosine_similarity(req_emb, up_emb)
            if sim >= similarity_threshold:
                matched = True
                break
        if not matched:
            missing_docs.append(req_doc)

    return {
        "process": process,
        "required_documents": required_docs,
        "uploaded_documents": uploaded_types,
        "missing_documents": missing_docs
    }

def cosine_similarity(vec1, vec2):
    import numpy as np
    return float(np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2)))
