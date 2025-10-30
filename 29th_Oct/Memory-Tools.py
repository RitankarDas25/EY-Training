# ============================================================
# Memory-Tools.py — Enhanced Conversational Mistral Agent
# ============================================================

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.schema import HumanMessage, AIMessage

# ------------------------------------------------------------
# 1. Load environment variables
# ------------------------------------------------------------
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
base_url = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")

if not api_key:
    raise ValueError("OPENROUTER_API_KEY not found in .env file")

# ------------------------------------------------------------
# 2. Initialize the Mistral model via OpenRouter
# ------------------------------------------------------------
llm = ChatOpenAI(
    model="mistralai/mistral-7b-instruct",
    temperature=0.4,
    max_tokens=512,
    api_key=api_key,
    base_url=base_url,
)

# ------------------------------------------------------------
# 3. Helper tools
# ------------------------------------------------------------
def multiply(a: int, b: int) -> str:
    """Multiply two integers."""
    return f"The result of {a} × {b} is {a * b}."

def greet(name: str) -> str:
    """Return a friendly greeting."""
    name = name.strip().replace('"', "").replace("'", "")
    return f"Hello {name}, welcome to the AI Agent demo! How are you doing today?"

def weather(city: str) -> str:
    """Simulated weather info."""
    conditions = {
        "dubai": "sunny with 33°C",
        "riyadh": "hot and dry with 36°C",
        "bengaluru": "cloudy with 27°C",
        "singapore": "humid with 30°C",
    }
    info = conditions.get(city.lower(), "not available right now")
    return f"The current weather in {city.title()} is {info}."

# ------------------------------------------------------------
# 4. Memory setup
# ------------------------------------------------------------
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# ------------------------------------------------------------
# 5. Conversational loop
# ------------------------------------------------------------
print("\n=== Start chatting with your Agent ===")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() == "exit":
        print("\nConversation ended.")
        break

    response_text = ""

    # ---------- Commands ----------
    try:
        if user_input.lower().startswith("multiply"):
            parts = user_input.split()
            a, b = int(parts[1]), int(parts[2])
            response_text = multiply(a, b)

        elif user_input.lower().startswith("greet"):
            name = " ".join(user_input.split()[1:]).strip()
            response_text = greet(name) if name else "Please provide a name."

        elif "my name is" in user_input.lower():
            name = user_input.split("is")[-1].strip()
            response_text = greet(name)

        elif "what" in user_input.lower() and "my name" in user_input.lower():
            messages = memory.load_memory_variables({}).get("chat_history", [])
            if messages:
                for msg in reversed(messages):
                    if isinstance(msg, AIMessage) and "Hello" in msg.content:
                        response_text = f"You told me earlier your name is {msg.content.split('Hello ')[1].split(',')[0]}."
                        break
                else:
                    response_text = "I don't know your name yet."
            else:
                response_text = "I don't know your name yet."

        elif user_input.lower().startswith("weather"):
            city = " ".join(user_input.split()[1:]).strip()
            response_text = weather(city) if city else "Please specify a city name."

        else:
            # Use LLM for natural conversation with memory context
            chat_history = memory.load_memory_variables({}).get("chat_history", [])
            response = llm.invoke(chat_history + [HumanMessage(content=user_input)])
            response_text = response.content

    except Exception as e:
        response_text = f"Error: {str(e)}"

    # ---------- Output ----------
    print(f"Agent: {response_text}")
    memory.save_context({"input": user_input}, {"output": response_text})
