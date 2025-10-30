import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.schema import HumanMessage

# ------------------------------------------------------------
# Load API Key
# ------------------------------------------------------------
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
base_url = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")

if not api_key:
    raise ValueError("OPENROUTER_API_KEY not found in .env file")

# ------------------------------------------------------------
# Initialize Mistral Model via OpenRouter
# ------------------------------------------------------------
llm = ChatOpenAI(
    model="mistralai/mistral-7b-instruct",
    temperature=0.5,
    max_tokens=300,
    api_key=api_key,
    base_url=base_url,
)

# ------------------------------------------------------------
# Memory to store conversation history
# ------------------------------------------------------------
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# ------------------------------------------------------------
# Tool functions
# ------------------------------------------------------------

def word_count(sentence):
    """Count words in a sentence."""
    words = sentence.split()
    return f"Your sentence has {len(words)} words."

def reverse_text(sentence):
    """Reverse the word order of a sentence."""
    words = sentence.split()
    reversed_sentence = " ".join(reversed(words))
    return reversed_sentence

def vocabulary_helper(word):
    """Return a synonym or definition of the word."""
    prompt = f"Provide a brief definition or synonym for the word '{word}'."
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content.strip()

def change_case(sentence, case_type):
    """Change case of a sentence (uppercase or lowercase)."""
    if case_type == "upper":
        return sentence.upper()
    elif case_type == "lower":
        return sentence.lower()
    else:
        return "Invalid case type. Use 'upper' or 'lower'."

def repeat_word(word, times):
    """Repeat a word a specified number of times."""
    return " ".join([word] * times)

# ------------------------------------------------------------
# Chatbot Loop
# ------------------------------------------------------------
print("\n=== Welcome to the Mini Language Utility Bot ===")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "exit":
        print("Goodbye 👋")
        break

    response = ""

    # Process commands
    if user_input.lower().startswith("count"):
        sentence = user_input.replace("count", "").strip()
        response = word_count(sentence)

    elif user_input.lower().startswith("reverse"):
        sentence = user_input.replace("reverse", "").strip()
        response = reverse_text(sentence)

    elif user_input.lower().startswith("define"):
        word = user_input.replace("define", "").strip()
        response = vocabulary_helper(word)

    elif user_input.lower().startswith("upper"):
        sentence = user_input.replace("upper", "").strip()
        response = change_case(sentence, "upper")

    elif user_input.lower().startswith("lower"):
        sentence = user_input.replace("lower", "").strip()
        response = change_case(sentence, "lower")

    elif user_input.lower().startswith("repeat"):
        parts = user_input.split()
        if len(parts) == 3 and parts[2].isdigit():
            word = parts[1]
            times = int(parts[2])
            response = repeat_word(word, times)
        else:
            response = "Please use the format: repeat <word> <number>"

    elif user_input.lower() == "history":
        messages = memory.load_memory_variables({}).get("chat_history", [])
        if messages:
            history = "\n".join([f"{msg['input']} → {msg['output']}" for msg in messages])
            response = f"History:\n{history}"
        else:
            response = "No history available."

    else:
        # Default chat with Mistral if no specific command
        response = llm.invoke([HumanMessage(content=user_input)]).content.strip()

    # Save context to memory
    memory.save_context({"input": user_input}, {"output": response})

    print(f"Agent: {response}")
