# Import relevant functionality
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
from math_tools import add, subtract, multiply, exponentiate, differentiate, integrate, solve_equation
from advanced_tools import capture_image

# Set the environment variable for the API key
load_dotenv()

# Create the agent
memory = MemorySaver()
model = ChatOpenAI(
    model="o4-mini",
)
search = TavilySearchResults(max_results=2)
tools = [search, add, subtract, multiply, exponentiate, differentiate, integrate, solve_equation, capture_image]
agent = create_react_agent(model, tools, checkpointer=memory)

# Use the agent
config = {"configurable": {"thread_id": "abc123"}}

# for step in agent.stream(
#     input={"messages": [HumanMessage(content="I live in sf.")]},
#     config=config,
#     stream_mode="values",
# ):
#     step["messages"][-1].pretty_print()

# for step in agent.stream(
#     input={"messages": [HumanMessage(content="What is the weather where I live?")]},
#     config=config,
#     stream_mode="values",
# ):
#     step["messages"][-1].pretty_print()

# for step in agent.stream(
#     input={"messages": [HumanMessage(content="What is 123.5 / 456?")]},
#     config=config,
#     stream_mode="values",
# ):
#     step["messages"][-1].pretty_print()

# for step in agent.stream(
#     input={"messages": [HumanMessage(content="What is the derivative of 1/5x^5 + x^2 + 3x + 5 + ln(x)?")]},
#     config=config,
#     stream_mode="values",
# ):
#     step["messages"][-1].pretty_print()

for step in agent.stream(
    input={"messages": [HumanMessage(content="Take an image of me with the camera.")]},
    config=config,
    stream_mode="values",
):
    step["messages"][-1].pretty_print()