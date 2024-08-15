# tools.py
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set the API key for the SerperDevTool
os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')

# Initialize the tool
tool = SerperDevTool()