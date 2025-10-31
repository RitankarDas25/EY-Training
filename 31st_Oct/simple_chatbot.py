import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# Load your .env file
load_dotenv()

# --- Configure OpenRouter ---
os.environ["OPENAI_API_KEY"] = os.getenv("OPENROUTER_API_KEY")
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"
os.environ["OPENAI_MODEL"] = "mistralai/mistral-7b-instruct"  # or any model you prefer

# --- Create the model ---
llm = ChatOpenAI(
    model=os.getenv("OPENAI_MODEL"),
    temperature=0.7
)

# --- Add memory ---
memory = ConversationBufferMemory()

# --- Create a conversation chain ---
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

print(" LangChain Memory Chatbot")
print("Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Goodbye! ")
        break

    response = conversation.predict(input=user_input)
    print(f"Bot: {response}\n")
