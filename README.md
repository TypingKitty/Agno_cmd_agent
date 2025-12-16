# Agno CommandLine Agent

A command-line tool that converts **plain English instructions** into **commandline prompts** and executes them locally using Agno with Groq.

---

## Features

- Execute any commandline operations using natural language
- Works as an interactive CLI
- Supports commands such as , clone any small flutter repo which uses mobile_scanner library or revert the last commit without reverting the changes
- Uses environment variables for secure credentials
- Retains previous interactions through an automatically created sqlite db.

---

## Setup

### 1. Create and activate virtual environment

```bash
python -m venv venv
source venv/Scripts/activate   # Windows
# or
source venv/bin/activate      # macOS / Linux
```

### 2. Install requirements

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root (do not commit this file):

```env
GROQ_API_KEY=your_groq_api_key
GITHUB_TOKEN=your_github_personal_access_token
```

## Run the Agent

```bash
python agent.py
```


