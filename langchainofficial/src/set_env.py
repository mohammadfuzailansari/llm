
import getpass
import os
from dotenv import load_dotenv

load_dotenv()  # This loads the environment variables from .env

# Read an environment variable
print(os.getenv("OPENAI_API_KEY"))
print(os.getenv("LANGCHAIN_TRACING_V2"))
print(os.getenv("LANGCHAIN_API_KEY"))