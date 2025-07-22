import os
from crewai_tools import HyperbrowserLoadTool
from dotenv import load_dotenv
load_dotenv()
hyperbrowser_tool = HyperbrowserLoadTool(api_key=os.getenv("HYPERBROWSER_API_KEY"))