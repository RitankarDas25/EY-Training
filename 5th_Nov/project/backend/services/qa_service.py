from langchain.chains import RetrievalQA

def build_qa_chain(vectordb, llm, k=5):
    retriever = vectordb.as_retriever(search_kwargs={"k": k})
    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

def answer_question(qa_chain, question):
    result = qa_chain.invoke({"query": question})
    answer = result["result"]
    sources = []
    for doc in result["source_documents"]:
        sources.append({
            "chunk_id": doc.metadata.get("chunk_id"),
            "excerpt": doc.page_content[:300]
        })
    return answer, sources
