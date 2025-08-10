from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
import config

def build_doc_type_chain():
    embeddings = HuggingFaceEmbeddings(model_name=config.EMBEDDINGS_MODEL)
    vectorstore = FAISS.load_local(config.VECTORSTORE_DIR, embeddings, allow_dangerous_deserialization=True)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    template = """
You are an ADGM document classifier.
Given the context and the document snippet, return ONLY the document type (short name).
If not sure, return "Unknown Document Type".

Context:
{context}

Document snippet:
{question}
"""
    prompt = PromptTemplate(input_variables=["context", "question"], template=template)

    llm = ChatGroq(
        groq_api_key=config.GROQ_API_KEY,
        model_name=config.GROQ_MODEL,
        temperature=0.2
    )

    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": prompt}
    )
