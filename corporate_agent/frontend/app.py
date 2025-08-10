import streamlit as st
import json
import requests

# =======================
# Backend API configuration
# =======================
BACKEND_URL = "http://127.0.0.1:7000"  # Change if backend is hosted elsewhere

# =======================
# Page Config
# =======================
st.set_page_config(page_title="Corporate Agent", layout="wide")
st.title("📄 Corporate Agent")

# =======================
# File Upload Section
# =======================
uploaded_files = st.file_uploader(
    "📥 Upload one or more DOCX documents",
    type=["docx"],
    accept_multiple_files=True
)

# =======================
# Analyze Button
# =======================
if uploaded_files:
    if st.button("🚀 Analyze Documents"):
        # Prepare files for API call
        files_payload = [
            (
                "files",
                (f.name, f.read(), "application/vnd.openxmlformats-officedocument.wordprocessingml.document")
            )
            for f in uploaded_files
        ]

        try:
            # Send request to FastAPI backend
            response = requests.post(f"{BACKEND_URL}/analyze-documents", files=files_payload)

            if response.status_code != 200:
                st.error(f"❌ API Error: {response.status_code} - {response.text}")
            else:
                data = response.json()

                # =======================
                # Display Combined Report
                # =======================
                combined_report = data.get("combined_report", {})
                reviewed_docs = data.get("reviewed_docs", [])

                st.subheader("🧾 Combined Analysis Report")
                st.json(combined_report)

                # =======================
                # Display Compliance Issues
                # =======================
                st.subheader("⚠️ Compliance Issues Found")
                st.json(combined_report.get("issues_found", []))

                # =======================
                # Display Reviews
                # =======================
                st.subheader("💡 Review Summaries & Recommendations")
                st.json(combined_report.get("reviews", []))

                # =======================
                # Download Reviewed DOCX Files
                # =======================
                st.subheader("⬇️ Reviewed Documents")
                for doc in reviewed_docs:
                    fname = doc.get("filename", "reviewed.docx")
                    bytes_data = bytes.fromhex(doc.get("content", ""))
                    st.download_button(
                        label=f"Download reviewed: {fname}",
                        data=bytes_data,
                        file_name=f"reviewed_{fname}",
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    )

                # =======================
                # Download Combined Report JSON
                # =======================
                st.download_button(
                    label="⬇️ Download Combined JSON Report",
                    data=json.dumps(combined_report, indent=2),
                    file_name="combined_report.json",
                    mime="application/json"
                )

        except Exception as e:
            st.error(f"❌ Error processing: {str(e)}")

else:
    st.info("📄 Please upload one or more DOCX files to start.")
