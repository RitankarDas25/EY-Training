import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings

load_dotenv()

def get_env_vars():
    api_key = os.getenv("OPENROUTER_API_KEY")
    base_url = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
    if not api_key:
        raise ValueError("Missing OPENROUTER_API_KEY in .env")
    return api_key, base_url

def get_llm(model_name="gpt-4o-mini", temperature=0.2):
    api_key, base_url = get_env_vars()
    return ChatOpenAI(
        model_name=model_name,
        temperature=temperature,
        openai_api_key=api_key,
        openai_api_base=base_url,
    )

def get_embeddings():
    api_key, base_url = get_env_vars()
    return OpenAIEmbeddings(
        openai_api_key=api_key,
        openai_api_base=base_url
    )
