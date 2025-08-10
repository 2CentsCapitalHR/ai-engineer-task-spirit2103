from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from docx_processing import analyze_and_comment_docx_batch
import json
import uvicorn


app = FastAPI(title="Corporate Agent API", version="1.0")

# CORS for local dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze-documents")
async def analyze_documents(files: list[UploadFile] = File(...)):
    doc_bytes_list = []
    filenames = []
    for file in files:
        content = await file.read()
        doc_bytes_list.append(content)
        filenames.append(file.filename)

    reviewed_docs, combined_report = analyze_and_comment_docx_batch(
        doc_bytes_list,
        uploaded_filenames=filenames
    )

    # Convert reviewed_docs into base64 for API return
    reviewed_docs_base64 = []
    for fname, bytes_data in reviewed_docs:
        reviewed_docs_base64.append({
            "filename": fname,
            "content": bytes_data.hex()  # return as hex string
        })

    return {
        "combined_report": combined_report,
        "reviewed_docs": reviewed_docs_base64
    }
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=7000)
