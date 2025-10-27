import os
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

# 1. Load environment variables from .env
load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
base_url = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")

if not api_key:
    raise ValueError("OPENROUTER_API_KEY not found in .env file")

# 2. Initialize LangChain model pointing to OpenRouter
llm = ChatOpenAI(
    model="meta-llama/llama-3.1-70b-instruct",  # Model name provided
    temperature=0.7,
    max_tokens=256,
    api_key=api_key,
    base_url=base_url,
)


# 4. Streamlit UI
st.title("Jarvis")
st.write("Welcome! Ask me anything!")

# Input field for user's question
user_input = st.text_area("Ask a question:", height=100)

# Button to submit question
if st.button("Submit"):
    if user_input:
        # 5. Define messages
        messages = [
            SystemMessage(content="You are a helpful and concise AI assistant."),
            HumanMessage(content=user_input),  # Use user input directly
        ]

        # 6. Invoke model and display response
        try:
            response = llm.invoke(messages)
            st.subheader("My Response:")
            st.write(response.content.strip() or "(no content returned)")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a question to submit.")
