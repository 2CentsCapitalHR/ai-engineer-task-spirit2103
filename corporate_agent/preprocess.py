import os
import glob
import json
from tqdm import tqdm
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructuredPDFLoader, PyPDFLoader, Docx2txtLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import config


def load_documents(source_dir):
    """Loads PDF and DOCX files from the given directory."""
    docs = []
    patterns = ["*.docx", "*.doc", "*.pdf"]

    for pat in patterns:
        for path in tqdm(glob.glob(os.path.join(source_dir, pat)), desc=f"Loading {pat}"):
            if path.lower().endswith(".pdf"):
                try:
                    loader = PyPDFLoader(path)  # Faster, better for text PDFs
                except Exception:
                    loader = UnstructuredPDFLoader(path)  # Fallback for scanned/image PDFs
            else:
                loader = Docx2txtLoader(path)

            try:
                loaded = loader.load()
                for d in loaded:
                    d.metadata["source"] = os.path.basename(path)
                docs.extend(loaded)
            except Exception as e:
                print(f"❌ Error reading {path}: {e}")

    return docs


def build_index():
    """Splits documents, creates embeddings, and saves FAISS index."""
    print("📂 Loading ADGM source documents from:", config.ADGM_SOURCES_DIR)
    docs = load_documents(config.ADGM_SOURCES_DIR)

    if not docs:
        raise RuntimeError("❌ No ADGM source docs found. Put PDFs/DOCX into data/adgm_sources/")

    print(f"✅ Loaded {len(docs)} documents. Splitting into chunks...")

    # Split text into chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    chunks = splitter.split_documents(docs)

    print(f"✅ Created {len(chunks)} chunks. Generating embeddings...")

    # Create embeddings
    embeddings = HuggingFaceEmbeddings(model_name=config.EMBEDDINGS_MODEL)

    # Build FAISS index
    vectorstore = FAISS.from_documents(chunks, embeddings)

    # Save index
    os.makedirs(config.VECTORSTORE_DIR, exist_ok=True)
    vectorstore.save_local(config.VECTORSTORE_DIR)

    # Save meta info
    meta = {"n_chunks": len(chunks), "n_docs": len(docs)}
    with open(os.path.join(config.VECTORSTORE_DIR, "meta.json"), "w") as f:
        json.dump(meta, f)

    print(f"🎯 Index built with {len(chunks)} chunks from {len(docs)} documents.")


if __name__ == "__main__":
    build_index()
