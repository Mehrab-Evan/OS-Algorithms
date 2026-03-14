# app.py
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver
from dotenv import load_dotenv
import os, json

import subprocess
def open_application(app_name: str):
    """
    Opens an application on MacOS by name.
    Example: Telegram, Google Chrome, WhatsApp
    """
    try:
        subprocess.run(["open", "-a", app_name])
        return f"{app_name} opened successfully."
    except Exception as e:
        return f"Error opening {app_name}: {str(e)}"
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
You are a personal assistant for my pc. My pc name is MeMac. It has 16GB RAM and runs Mac M3 Air.

Your job is to open applications when the user asks.

Use the tool open_application and pass the app name.

Examples:
- If user says "open telegram", pass "Telegram"
- If user says "open whatsapp", pass "WhatsApp"
- If user says "open chrome", pass "Google Chrome"
"""

# Create agent
agent = create_agent(
    model,
    tools=[open_application],
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

