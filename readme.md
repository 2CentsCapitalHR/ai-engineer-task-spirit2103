# 🏛️ ADGM Corporate Agent – RAG + Groq AI

An AI-powered compliance assistant that processes **ADGM corporate documents** (`.docx`),  
detects the **document type**, checks **regulatory compliance**, identifies **missing documents**,  
and adds **AI review comments** directly into the Word file.

Built with:
- **[Streamlit](https://streamlit.io/)** – interactive frontend
- **[LangChain](https://www.langchain.com/)** + **[LangGraph](https://github.com/langchain-ai/langgraph)** – agent orchestration
- **Groq API** with **Qwen LLM** – fast, low-latency AI reasoning
- **HuggingFace Embeddings** – semantic matching for inline comments
- **Python-Docx** – DOCX reading & writing

---

## 📌 Features
✅ **Multi-file upload** – Analyze multiple `.docx` files at once  
✅ **Document type detection** – Using Groq LLM + keyword fallback  
✅ **Compliance checking** – Against ADGM regulatory checklists  
✅ **Missing document detection** – Based on company process type  
✅ **AI-annotated DOCX** – Inline comments with improvement suggestions  
✅ **JSON compliance report** – For easy system integration  
✅ **Fuzzy matching** – Handles variations in document titles  


---

## 🚀 Installation & Setup

### 1️. CLONE THE GIT REPO
```bash
git clone https://github.com/<your-username>/adgm-corporate-agent.git
cd adgm-corporate-agent

### 2. CREATE AND ACTIVATE VIRTUAL ENVIRNMENT
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

### 3. iNSTALL DEPENDENCY
pip install -r requirements.txt

### 4. CREATE .ENV IN HE ROOT FOLDER
GROQ_API_KEY=your_groq_api_key_here

### 5. RUNNING THE APP
1. python preprocess.py

2. streamlit run app.py
