import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL", "meta-llama/llama-4-maverick-17b-128e-instruct")
EMBEDDINGS_MODEL = os.getenv("EMBEDDINGS_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
VECTORSTORE_DIR = os.getenv("VECTORSTORE_DIR", "data/adgm_index")
ADGM_SOURCES_DIR = os.getenv("ADGM_SOURCES_DIR", "data/adgm_sources")
