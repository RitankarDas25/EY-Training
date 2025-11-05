import streamlit as st
import requests
import tempfile

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Research Paper Summarizer", layout="wide")
st.title("📘 Research Paper Summarizer + Q&A (FastAPI + Streamlit)")

uploaded = st.file_uploader("Upload Research Paper (PDF)", type=["pdf"])

if uploaded:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded.read())
        pdf_path = tmp.name

    st.success("PDF uploaded successfully!")

    if st.button("Generate Summary"):
        with open(pdf_path, "rb") as f:
            resp = requests.post(f"{API_URL}/summarize/", files={"file": f})
        summary = resp.json().get("summary")
        st.subheader("Summary")
        st.write(summary)

    st.subheader("Ask a Question")
    q = st.text_input("Your question about the paper:")
    if st.button("Ask"):
        if q.strip():
            with open(pdf_path, "rb") as f:
                resp = requests.post(f"{API_URL}/qa/", data={"question": q}, files={"file": f})
            data = resp.json()
            st.markdown(f"**Answer:** {data['answer']}")
            with st.expander("Sources"):
                for s in data["sources"]:
                    st.markdown(f"- **{s['chunk_id']}**: {s['excerpt']}...")
