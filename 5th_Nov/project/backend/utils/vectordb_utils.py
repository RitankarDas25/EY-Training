from langchain.vectorstores import Chroma
from langchain.docstore.document import Document

def create_vectorstore(chunks, persist_directory, embedding_model):
    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=persist_directory
    )
    vectordb.persist()
    return vectordb
