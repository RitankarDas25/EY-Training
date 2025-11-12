from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
base_url = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")

llm = ChatOpenAI(
    model="gpt-4o-mini",
    base_url=base_url,
    api_key=api_key,
    temperature=0.4
)

def chat(prompt: str, system="You are a business analyst."):
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", system),
        ("user", "{user_input}")
    ])
    chain = prompt_template | llm
    return chain.invoke({"user_input": prompt}).content
