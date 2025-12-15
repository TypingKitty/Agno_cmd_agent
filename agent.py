import asyncio
import os
from dotenv import load_dotenv
from agno.agent import Agent
from mcp_server_shell import ShellTool
from agno.models.groq import Groq
from agno.db.sqlite import SqliteDb


async def run_shell_agent()->None:
    load_dotenv()
    db = SqliteDb(db_file="tmp/agent_memory.db")
    try:
        print("Hi, I am a Git expert agent. How can I assist you today?")
        while(True):
            message=  input()
            if(message.lower() in ["exit","quit"]):
                print("Exiting the agent. Goodbye!")
                break
            agent = Agent(model= Groq(id="llama-3.1-8b-instant"),session_id="my session" ,db = db , add_history_to_context= True ,tools = [ShellTool], instructions="you are a git/github expert . you convert user's prompt into git commands which you then execute using ShellTool. PAT is loaded under GITHUB_KEY. And only use the tool given")

            print(f"Agent is running with the custom Shell Executor tool...")
            await agent.aprint_response(message, stream=True)
            print("-" * 50)
            
    except Exception as e:
        print(f"\nAn error occurred: {e}")



if __name__ == "__main__":
    
    asyncio.run(run_shell_agent())