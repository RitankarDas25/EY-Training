import os
import requests
from dotenv import load_dotenv
from langchain.tools import tool
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType

# Step 1: Load environment variables
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENROUTER_API_KEY")
os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

# Step 2: Create a custom tool to fetch weather data
@tool("get_weather", return_direct=True)
def get_weather(city: str) -> str:
    """
    Fetch the current weather for a given city using OpenWeather API.
    """
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            return f"Could not find weather info for {city}. Check spelling."

        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]

        return (
            f"Current weather in {city.title()}:\n"
            f"- Condition: {weather}\n"
            f"- Temperature: {temp}°C (Feels like {feels_like}°C)\n"
            f"- Humidity: {humidity}%"
        )
    except Exception as e:
        return f"Error fetching weather: {str(e)}"

# Step 3: Initialize an LLM (You can use OpenRouter, OpenAI, or any supported model)
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.5)

# Step 4: Initialize the agent with the weather tool
tools = [get_weather]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Step 5: Take user input dynamically
if __name__ == "__main__":
    city = input("Enter a city name: ")
    result = agent.run(f"What is the current weather in {city}?")
    print("\n🔍 AI Agent Response:\n", result)
