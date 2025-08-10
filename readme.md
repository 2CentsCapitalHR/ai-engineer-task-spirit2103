# 📄 Corporate Agent – ADGM Document Compliance Analyzer

**Corporate Agent** is an AI-powered system that analyzes corporate DOCX documents for **completeness**, **compliance**, and **recommendations** based on **ADGM regulations**.  
It uses **FastAPI** for the backend and **Streamlit** for the frontend, with AI models to detect document type, review content, and flag compliance issues.

---

## 🛠 Tech Stack
- **Backend:** FastAPI, LangChain, HuggingFace, Groq
- **Frontend:** Streamlit
- **AI Models:** all-MiniLM-L6-v2, Groq LLM
- **Document Processing:** python-docx
- **Vector Search:** FAISS
- **Other:** NumPy, Pandas, python-dotenv, Requests

---

## 🚀 Features
- 📂 **Multi-file DOCX upload**
- 🤖 **AI-powered document type detection**
- ✅ **Automated compliance checks** (against ADGM regulations)
- 📝 **Detailed AI-generated reviews & recommendations**
- 💬 **AI comments added directly into DOCX**
- 📥 **Download reviewed DOCX & JSON reports**
- 🔄 **Backend–frontend separation for scalability**

---

## 🚀 Installation & Setup

### 1️. CLONE THE GIT REPO
```bash
git clone https://github.com/<your-username>/adgm-corporate-agent.git
cd adgm-corporate-agent

2. CREATE AND ACTIVATE VIRTUAL ENVIRNMENT
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

3. iNSTALL DEPENDENCY
pip install -r requirements.txt

4. CREATE .env IN HE ROOT FOLDER
GROQ_API_KEY=your_groq_api_key_here

### 5. RUNNING THE APP
1. python preprocess.py

2.  cd backend
    uvicorn main:app --port 7000 --reload

3.  cd frontend
    streamlit run app.py

