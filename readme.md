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

## ⚙️ Installation & Setup

Follow these steps **exactly** to set up and run Corporate Agent.

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/adgm-corporate-agent.git
cd adgm-corporate-agent

2️⃣ Create and Activate Virtual Environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
pip install --upgrade pip
pip install -r requirements.txt

4️⃣ Create .env File in the Root Folder
GROQ_API_KEY=your_groq_api_key_here
EMBEDDINGS_MODEL=all-MiniLM-L6-v2
VECTORSTORE_DIR=vectorstore
ADGM_SOURCES_DIR=data/adgm_sources
GROQ_MODEL=meta-llama/lama-4-maverick-17b-128e-instruct

5️⃣ Prepare ADGM Knowledge Base
Put all your ADGM regulation documents (DOCX/PDF) inside:
data/adgm_sources/

6️⃣ Build the Vectorstore Index
This step processes ADGM source docs and builds embeddings for retrieval.
python preprocess.py

7️⃣ Start the Backend Server (FastAPI)
cd backend
uvicorn main:app --reload --port 7000
Backend will be available at:
http://127.0.0.1:7000

8️⃣ Start the Frontend App (Streamlit)
Open a new terminal in the project folder:
cd frontend
streamlit run app.py

9️⃣ Using the App
Open the Streamlit link in your browser (usually http://localhost:8501).
Upload one or more DOCX documents.
Click "🚀 Analyze Documents".

View:
Combined Compliance Report
Red Flags & Issues
Recommendations

Download:
Reviewed DOCX (with AI comments)
Combined JSON Report