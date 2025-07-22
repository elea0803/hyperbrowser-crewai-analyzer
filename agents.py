from crewai import Agent
from langchain_ollama import ChatOllama
from tool import hyperbrowser_tool

MODEL_NAME = "ollama/llama3.2:3b"
OLLAMA_BASE_URL = "http://localhost:11434"
MAX_RETRIES = 2

def get_llm_provider():
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            llm = ChatOllama(
                model=MODEL_NAME,
                base_url=OLLAMA_BASE_URL,
                temperature=0.7,
                verbose=True,
                provider="ollama"
            )
            return llm
        except Exception as e:
            print(f"Ollama LLM initialization failed (attempt {attempt}): {e}")
            if attempt < MAX_RETRIES:
                import time
                time.sleep(2 ** attempt)
            else:
                raise RuntimeError(
                    "Failed to initialize the Ollama LLM after multiple retries. "
                    "Please ensure Ollama is running and your model is available."
                ) from e

ollama_llm = get_llm_provider()

# Define the agents for the crewAI system
researcher = Agent(
    role="Expert Web Researcher",
    goal="Scrape the full textual content from a given URL using Hyperbrowser.",
    backstory="A meticulous researcher who uses cutting-edge tools to extract clean, complete data from web pages.",
    llm=ollama_llm,
    tools=[hyperbrowser_tool],
    allow_delegation=False,
    verbose=True
)

analyst = Agent(
    role="Senior Content Analyst",
    goal="Analyze scraped text to extract a summary, key topics, and sentiment.",
    backstory="An expert analyst with a sharp eye for detail, capable of distilling complex information into clear insights.",
    llm=ollama_llm,
    allow_delegation=False,
    verbose=True
)

report_assembler = Agent(
    role="Chief Report Editor",
    goal="Assemble the final report, ensuring it includes the full article and the analysis.",
    backstory="A detail-oriented editor responsible for compiling final reports that are comprehensive and easy to read.",
    llm=ollama_llm,
    allow_delegation=True,
    verbose=True
)
