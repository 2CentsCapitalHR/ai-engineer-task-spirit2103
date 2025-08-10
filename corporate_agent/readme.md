🏢 ADGM-Compliant Corporate Agent (RAG + Groq + Streamlit)
📌 Overview
The ADGM-Compliant Corporate Agent is an AI-powered document analysis tool designed to review corporate compliance documents against ADGM (Abu Dhabi Global Market) regulations.

It uses:

Retrieval-Augmented Generation (RAG) for context-aware AI responses.

Groq-powered LLMs for fast and accurate reasoning.

Fuzzy matching to identify document types and detect missing required documents.

Streamlit as the interactive front-end.

DOCX annotation to highlight compliance issues directly inside uploaded files.

✨ Features
✅ Multi-file DOCX upload (process multiple corporate documents in one run)
✅ Automatic document type detection (via AI + keyword matching)
✅ RAG-based compliance checking using Groq LLM
✅ Fuzzy matching against checklists to determine missing required documents
✅ AI review summaries with recommendations
✅ Direct DOCX annotations with inline AI comments
✅ Downloadable combined compliance report in JSON format
✅ Download reviewed & annotated DOCX files
✅ Streamlit-powered dashboard UI

📂 Project Structure
bash
Copy code
project/
│
├── app.py                      # Streamlit frontend
├── docx_processing.py          # Core processing logic (AI + compliance checks)
│
├── chains/
│   ├── doc_type_chain.py        # AI prompt chain for doc type detection
│   ├── review_chain.py          # AI prompt chain for document review
│   ├── compliance_chain.py      # AI prompt chain for compliance checking
│
├── utils.py                     # Utility functions & checklists
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
⚙️ Installation
1️⃣ Clone the Repository
bash
Copy code
git clone https://github.com/your-username/adgm-corporate-agent.git
cd adgm-corporate-agent
2️⃣ Create a Virtual Environment
bash
Copy code
python -m venv venv
venv\Scripts\activate      
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Set Environment Variables
Create a .env file in the root directory and add:

env
Copy code
GROQ_API_KEY=your_groq_api_key_here
🚀 Running the App
bash
Copy code
streamlit run app.py
Then open the link in your browser (default: http://localhost:8501).

📤 Usage
1. Upload Documents
Click 📥 Upload one or more DOCX documents.

Select your ADGM-related corporate compliance files.

2. Click 🚀 Analyze Documents
AI will:

Detect document type.

Review for completeness.

Check for compliance issues.

Compare against checklist.

Annotate documents inline.

3. View Results
🧾 Combined Analysis Report — Process type, total uploaded, missing documents.

⚠️ Compliance Issues Found — Each detected issue with severity & suggestions.

💡 Review Summaries & Recommendations — AI-generated summaries & improvements.

⬇️ Reviewed Documents — Download AI-annotated DOCX files.

⬇️ Combined JSON Report — Download machine-readable report.

📑 Example Output
Combined Analysis Report

json
Copy code
{
  "process": "Private Company Limited",
  "documents_uploaded": 3,
  "required_documents": 4,
  "missing_documents": [
    "Articles of Association",
    "UBO Declaration Form"
  ],
  "issues_found": [
    {
      "document": "Board Resolution",
      "filename": "board_resolution.docx",
      "section": "MOVE OF COMPANY'S RECORDS TO REGISTERED OFFICE ADDRESS",
      "issue": "The resolution does not specify the type of company records...",
      "severity": "Medium",
      "suggestion": "Specify the type of company records being moved..."
    }
  ],
  "reviews": [
    {
      "document": "Board Resolution",
      "filename": "board_resolution.docx",
      "summary": "The resolution is missing specifics...",
      "recommendations": ["Add record type details", "Limit authority scope"]
    }
  ]
}
🔍 Technology Stack
Frontend: Streamlit

Backend AI: LangChain + Groq API

Embeddings: HuggingFace MiniLM

Document Processing: python-docx

📌 Notes
Fuzzy string matching is used so even partial document name matches will be detected in checklists.

AI model: openai/gpt-oss-120b via ChatGroq.

Supports multi-document batch analysis.

Works fully offline for annotation after AI outputs are generated.

📜 License
MIT License — You are free to use, modify, and distribute with attribution.