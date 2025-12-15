import asyncio
import os
from dotenv import load_dotenv
from textwrap import dedent

from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.mcp import MCPTools
from mcp import StdioServerParameters


load_dotenv()
LLM_MODEL = "llama-3.1-8b-instant"

github_server_params = StdioServerParameters(
    command="npx",
    args=["-y", "@modelcontextprotocol/server-github"],
    env={
        "GITHUB_TOKEN": os.getenv("GITHUB_TOKEN"), 
        "PATH": os.getenv("PATH") # Essential for finding npx/node on Windows
    }
)

# --- Agent Initialization ---
async def run_git_agent(message: str) -> None:
    async with MCPTools(server_params=github_server_params) as github_mcp_tools:
        git_assistant = Agent(
            model=Groq(id=LLM_MODEL),
            tools=[github_mcp_tools], 
            instructions=dedent(
                """
                You are a highly capable Git and GitHub assistant.
                You can execute all standard Git/GitHub commands like pull, commit,
                branch creation, and raising PRs.
                - When the user asks for a Git/GitHub action, use your tools.
                - Always be clear about the action you are taking.
                """
            ),
            markdown=True,
        )

        print(f"User: {message}\n---")
        await git_assistant.aprint_response(message, stream=True)
        print("---\n")

if __name__ == "__main__":
    commands = [
        "Clone from the 'main' branch of the agno-agi/agno repo.",
    ]

    for cmd in commands:
        asyncio.run(run_git_agent(cmd))