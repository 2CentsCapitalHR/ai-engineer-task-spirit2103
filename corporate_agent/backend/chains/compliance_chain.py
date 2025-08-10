# compliance_chain.py
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
import config

def build_compliance_chain():
    embeddings = HuggingFaceEmbeddings(model_name=config.EMBEDDINGS_MODEL)
    vectorstore = FAISS.load_local(config.VECTORSTORE_DIR, embeddings, allow_dangerous_deserialization=True)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

    template = """
You are an ADGM legal compliance assistant.
Use the provided context to check if the clause is compliant with ADGM regulations.

Return your answer ONLY as a **strict JSON array**.
Do not add any explanations, natural language text, or extra commentary outside the JSON.

Each array element must have the keys:
- "section" (string, section or clause identifier, or "N/A")
- "issue" (string, short description of the problem)
- "severity" (string, one of: Low, Medium, High)
- "suggestion" (string, suggested fix)
- "citation_if_any" (string, legal reference if applicable, else "")

If there are no issues, return [].

Context:
{context}

Clause:
{question}
"""
    prompt = PromptTemplate(input_variables=["context", "question"], template=template)

    llm = ChatGroq(
        groq_api_key=config.GROQ_API_KEY,
        model_name=config.GROQ_MODEL,
        temperature=0
    )

    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": prompt}
    )
