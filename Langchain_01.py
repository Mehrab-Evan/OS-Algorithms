from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver
from dotenv import load_dotenv
import os, json

import subprocess
def open_telegram():
    """This function calls a tool which opens whatsapp"""
    try:
        subprocess.run(["open", "-a", "Whatsapp"])
        print("Telegram opened successfully.")
    except Exception as e:
        print("Error opening Telegram:", e)

load_dotenv()

# Fetch environment variables
groq_api_key = os.getenv("GROQ_API")

# Initialize model
model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.7,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key=groq_api_key
)

# System prompt
system_prompt = """
You are a personal assistant for my pc. My pc name is MeMac. And it's 16 GB of RAM in Mac M3 Air.
Your main task is to serve me by opening various 
software. If I tell you to open whatsapp you will open whatsapp in my pc by calling the tool open_telegram.
"""

# Create agent
agent = create_agent(
    model,
    tools=[open_telegram],
    system_prompt=system_prompt,
    checkpointer=MemorySaver()
)

while(1) :
    message = input("Enter your message : ")
    user_id = '1'
    input_data = {"messages": [{"role": "user", "content": message}]}
    config = {"configurable": {"thread_id": user_id}}

    result = agent.invoke(input_data, config)
    # print(type(result))
    # print(type(agent))
    last_message = result['messages'][-1]
    # second_last_message = result['messages'][-3]
    print(result)
    print(last_message.content)

    # Here has to check if the second last message is json or not.
    # Cause without calling tool it is not json. Though Langgraph shows it's json altime
    # isToolResponse = is_visualization_tool_response(second_last_message)
    # print(isToolResponse)
