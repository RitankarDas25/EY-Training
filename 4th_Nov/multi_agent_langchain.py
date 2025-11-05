"""
Multi-Agent System using LangChain + Mistral via OpenRouter
-----------------------------------------------------------
1. Research Agent - gathers information
2. Summarizer Agent - condenses the info
3. Notifier Agent - outputs result
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

# ---------- LOAD ENV ----------
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENROUTER_API_KEY")
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"

MODEL_NAME = "mistralai/mistral-7b-instruct"
OUTPUT_MODE = "console"  # or "file"
OUTPUT_FILE = "summary_output.txt"

# ---------- MODEL SETUP ----------
llm = ChatOpenAI(
    model=MODEL_NAME,
    base_url=os.environ["OPENAI_API_BASE"],
    api_key=os.environ["OPENAI_API_KEY"],
    temperature=0.7,
    max_tokens=1000,
)

# ---------- AGENT 1: RESEARCH ----------
def research_agent(topic: str) -> str:
    """Collects factual and relevant research on a topic."""
    prompt = ChatPromptTemplate.from_template(
        "You are a factual research assistant. Write a comprehensive summary of the topic below, "
        "covering latest advancements, use cases, and real-world impact.\n\nTopic: {topic}"
    )
    messages = prompt.format_messages(topic=topic)
    response = llm.invoke(messages)
    content = getattr(response, "content", None)
    return content.strip() if content else str(response)

# ---------- AGENT 2: SUMMARIZER ----------
def summarizer_agent(research_text: str) -> str:
    """Summarizes the research into a concise form."""
    prompt = ChatPromptTemplate.from_template(
        "Summarize the following research into 5 clear sentences, focusing on accuracy and clarity:\n\n{research_text}"
    )
    messages = prompt.format_messages(research_text=research_text)
    response = llm.invoke(messages)
    content = getattr(response, "content", None)
    return content.strip() if content else str(response)

# ---------- AGENT 3: NOTIFIER ----------
def notifier_agent(summary_text: str, mode: str = "console"):
    """Outputs the summary."""
    if mode == "file":
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write("=== RESEARCH SUMMARY ===\n\n")
            f.write(summary_text)
        print(f" Summary saved to {OUTPUT_FILE}")
    else:
        print("\n--- RESEARCH SUMMARY ---\n")
        print(summary_text or "⚠️ No summary returned from model.")

# ---------- ORCHESTRATOR ----------
def run_multi_agent_system(topic: str):
    print(f" Starting multi-agent workflow for topic: {topic}\n")

    research_data = research_agent(topic)
    print(" Research completed.\n")

    summary = summarizer_agent(research_data)
    print(" Summarization completed.\n")

    notifier_agent(summary, mode=OUTPUT_MODE)
    print("\n Notification completed.\n")

# ---------- RUN ----------
if __name__ == "__main__":
    topic = "Applications of Generative AI in Healthcare"
    run_multi_agent_system(topic)
