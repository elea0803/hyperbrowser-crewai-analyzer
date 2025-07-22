import os
from dotenv import load_dotenv
load_dotenv()
print(os.getenv("HYPERBROWSER_API_KEY"))
