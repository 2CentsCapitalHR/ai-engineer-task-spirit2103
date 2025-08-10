import streamlit as st
import json
from docx_processing import analyze_and_comment_docx_batch

st.set_page_config(page_title="Corporate Agent", layout="wide")
st.title("📄 Corporate Agent")

uploaded_files = st.file_uploader(
    "📥 Upload one or more DOCX documents",
    type=["docx"],
    accept_multiple_files=True
)

if uploaded_files:
    if st.button("🚀 Analyze Documents"):
        doc_bytes_list = []
        filenames = []
        for f in uploaded_files:
            content = f.read()
            doc_bytes_list.append(content)
            filenames.append(f.name)

        try:
            reviewed_docs, combined_report = analyze_and_comment_docx_batch(
                doc_bytes_list,
                uploaded_filenames=filenames
            )

            st.subheader("🧾 Combined Analysis Report")
            st.json(combined_report)

            st.subheader("⚠️ Compliance Issues Found")
            st.json(combined_report.get("issues_found", []))

            st.subheader("💡 Review Summaries & Recommendations")
            st.json(combined_report.get("reviews", []))

            st.subheader("⬇️ Reviewed Documents")
            for fname, bytes_data in reviewed_docs:
                st.download_button(
                    label=f"Download reviewed: {fname}",
                    data=bytes_data,
                    file_name=f"reviewed_{fname}",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )

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
