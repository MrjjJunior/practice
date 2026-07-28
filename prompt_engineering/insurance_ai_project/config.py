"""
config.py
---------
Central configuration for the project.

We use Groq's OpenAI-compatible endpoint, so we talk to it with the
regular `openai` Python SDK — we just point `base_url` at Groq instead
of at OpenAI, and use a Groq API key.

Set your key as an environment variable before running anything:

    export GROQ_API_KEY="gsk_..."

(or put it in a .env file — see .env.example)
"""

import os
from openai import OpenAI

# Load a .env file if python-dotenv is installed (optional convenience).
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
GROQ_BASE_URL = "https://api.groq.com/openai/v1"

# Any current Groq-hosted model works. llama-3.3-70b-versatile is a good
# default: fast, cheap, and reliable at following JSON-only instructions.
MODEL_NAME = os.environ.get("GROQ_MODEL", "llama-3.3-70b-versatile")

if not GROQ_API_KEY:
    raise RuntimeError(
        "GROQ_API_KEY is not set. Run `export GROQ_API_KEY=your_key_here` "
        "or add it to a .env file before starting the app."
    )

client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url=GROQ_BASE_URL,
)