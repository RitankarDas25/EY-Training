from tqdm import tqdm
from langchain.prompts import PromptTemplate

MAP_PROMPT = PromptTemplate(
    input_variables=["chunk"],
    template="Summarize this research text chunk briefly (2–3 sentences) focusing on objectives, methods, and findings:\n\n{chunk}\n\nSummary:"
)

REDUCE_PROMPT = PromptTemplate(
    input_variables=["summaries"],
    template="Combine the following summaries into one structured summary with:\n"
             "- One-sentence main contribution\n"
             "- 3–4 bullet highlights\n"
             "- One short paragraph summary\n\n{summaries}\n\nStructured summary:"
)

def map_reduce_summary(chunks, llm):
    summaries = []
    for chunk in tqdm(chunks, desc="Summarizing chunks"):
        prompt = MAP_PROMPT.format(chunk=chunk.page_content)
        resp = llm.invoke(prompt)
        summaries.append(resp.content.strip())

    joined = "\n\n".join(summaries)
    final_resp = llm.invoke(REDUCE_PROMPT.format(summaries=joined))
    return final_resp.content.strip()
