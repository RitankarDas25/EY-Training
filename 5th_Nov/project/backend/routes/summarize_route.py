from fastapi import APIRouter, UploadFile
import tempfile
import time
from ..utils.pdf_utils import load_pdf, chunk_documents
from ..utils.llm_utils import get_llm
from ..services.summarize_service import map_reduce_summary

router = APIRouter(prefix="/summarize", tags=["Summarization"])

@router.post("/")
async def summarize_pdf(file: UploadFile):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(await file.read())
        pdf_path = tmp.name

    docs = load_pdf(pdf_path)
    chunks = chunk_documents(docs)
    llm = get_llm()
    summary = map_reduce_summary(chunks, llm)

    return {"summary": summary}
