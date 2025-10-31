import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew

# ========================
# Environment Setup
# ========================
load_dotenv()

os.environ["CREWAI_USE_LITELLM"] = "true"
os.environ["OPENAI_API_KEY"] = os.getenv("OPENROUTER_API_KEY")
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"
os.environ["LITELLM_MODEL"] = "mistralai/mistral-7b-instruct"

# ========================
# User Input
# ========================
dataset_description = input("Enter a dataset description: ")

# ========================
# Agents
# ========================
data_analyzer = Agent(
    role="Data Analyst",
    goal="Analyze dataset descriptions and extract key insights, trends, or issues.",
    backstory="A skilled data scientist who identifies trends and patterns quickly."
)

strategy_planner = Agent(
    role="Business Strategist",
    goal="Create actionable strategies based on the findings from the data analyst.",
    backstory="A strategist who converts insights into clear, results-oriented plans."
)

# ========================
# Tasks
# ========================
task1 = Task(
    description=f"Analyze this dataset: {dataset_description}. Identify key trends, patterns, and anomalies.",
    expected_output="A list of insights or findings from the dataset.",
    agent=data_analyzer
)

task2 = Task(
    description="Using the previous analysis, create 3 practical business strategies to improve performance.",
    expected_output="A short strategy document listing 3 business strategies.",
    agent=strategy_planner,
    context=[task1]  # Agent chaining: uses Task1 output
)

# ========================
# Crew Execution
# ========================
crew = Crew(
    agents=[data_analyzer, strategy_planner],
    tasks=[task1, task2],
    verbose=True
)

result = crew.kickoff()

print("\n Final Output:\n")
print(result)
