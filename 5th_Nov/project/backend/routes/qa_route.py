from fastapi import APIRouter, UploadFile, Form
import tempfile, time
from ..utils.llm_utils import get_llm, get_embeddings
from ..utils.pdf_utils import load_pdf, chunk_documents
from ..utils.vectordb_utils import create_vectorstore
from ..services.qa_service import build_qa_chain, answer_question

router = APIRouter(prefix="/qa", tags=["QuestionAnswering"])

@router.post("/")
async def qa_on_paper(file: UploadFile, question: str = Form(...)):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(await file.read())
        pdf_path = tmp.name

    docs = load_pdf(pdf_path)
    chunks = chunk_documents(docs)
    embeddings = get_embeddings()
    persist_dir = f"vectorstores/session_{int(time.time())}"
    vectordb = create_vectorstore(chunks, persist_dir, embeddings)
    llm = get_llm()
    qa_chain = build_qa_chain(vectordb, llm)
    answer, sources = answer_question(qa_chain, question)

    return {"answer": answer, "sources": sources}
