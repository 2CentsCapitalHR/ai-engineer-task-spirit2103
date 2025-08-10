import config
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate

def build_review_chain():
    # Load embeddings
    embeddings = HuggingFaceEmbeddings(model_name=config.EMBEDDINGS_MODEL)

    # Load FAISS index
    vectorstore = FAISS.load_local(
        config.VECTORSTORE_DIR,
        embeddings,
        allow_dangerous_deserialization=True
    )

    # Retriever (smaller k for efficiency)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

    # === Updated Prompt for Structured JSON Output ===
    template = """
You are an ADGM legal document reviewer.
Given the provided context and the document content, evaluate the document's completeness and correctness.

Return ONLY a **strict JSON object** with the following keys:
- "summary": (string) concise summary of the document's overall compliance status.
- "recommendations": (array) list of strings, each a specific suggestion to improve compliance, fix issues, or clarify clauses.

Do not add any text outside the JSON object.
Do not include markdown.
Do not include explanations or conversational text.

Context:
{context}

Document content:
{question}
"""
    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template=template
    )

    # Groq LLM
    llm = ChatGroq(
        groq_api_key=config.GROQ_API_KEY,
        model_name=config.GROQ_MODEL,
        temperature=0
    )

    # RetrievalQA chain
    review_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": prompt},
        return_source_documents=False
    )

    return review_chain
