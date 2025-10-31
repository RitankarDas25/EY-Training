import os
from dotenv import load_dotenv
from datetime import datetime
from langchain.tools import tool
from langchain_community.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, AgentType

# ======================================================
# 1 Setup
# ======================================================
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENROUTER_API_KEY")
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"
os.environ["OPENAI_MODEL"] = "mistralai/mistral-7b-instruct"

# ======================================================
# 2 Define Tools
# ======================================================

@tool("get_time", return_direct=True)
def get_time(input_text: str) -> str:
    """Get the current date and time."""
    return f"The current time is {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

@tool("calculator", return_direct=True)
def calculator(expression: str) -> str:
    """Evaluate a simple math expression."""
    try:
        result = eval(expression)
        return f"The answer is {result}"
    except Exception:
        return "Sorry, I couldn't calculate that."

@tool("word_count", return_direct=True)
def word_count(text: str) -> str:
    """Count how many words are in a given sentence."""
    words = len(text.split())
    return f"Your sentence has {words} words."

@tool("case_converter", return_direct=True)
def case_converter(text: str) -> str:
    """Convert text to uppercase or lowercase based on keywords."""
    if "upper" in text.lower():
        return text.replace("upper", "").strip().upper()
    elif "lower" in text.lower():
        return text.replace("lower", "").strip().lower()
    else:
        return "Please specify whether to convert to 'upper' or 'lower'."

# ======================================================
# 3 Initialize Model & Agent
# ======================================================
llm = ChatOpenAI(
    model=os.getenv("OPENAI_MODEL"),
    temperature=0.3
)

tools = [get_time, calculator, word_count, case_converter]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# ======================================================
# 4 Run Interactive Loop
# ======================================================
print(" LangChain Tool Orchestration Demo (4 Tools Active)")
print("Available tools:")
print("- get_time → get current time")
print("- calculator → do math (e.g. 5 * (3 + 2))")
print("- word_count → count words in a sentence")
print("- case_converter → convert to upper/lowercase")
print("Type 'exit' to quit.\n")

while True:
    query = input("You: ")
    if query.lower() == "exit":
        print("Goodbye! ")
        break
    response = agent.run(query)
    print("Agent:", response, "\n")
