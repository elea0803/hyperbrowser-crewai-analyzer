#tasks.py

from crewai import Task
from agents import researcher, analyst, report_assembler
from tool import hyperbrowser_tool

scrape_task = Task(
    description=(
        "Scrape the full content of the URL: {url}. "
        "To do this, you MUST use the 'Hyperbrowser web load tool'. "
        "When using the tool, set the 'operation' argument to 'scrape'. "
        "The output should be the raw markdown content of the page."
    ),
    expected_output="The complete, raw markdown content of the web page.",
    agent=researcher,
    tools=[hyperbrowser_tool]
)

analysis_task = Task(
    description="Analyze the provided text. Create a concise summary, a bullet-point list of key topics, and a one-sentence sentiment analysis.",
    expected_output="A structured analysis containing a summary, key topics, and sentiment.",
    agent=analyst,
    context=[scrape_task]
)

report_task = Task(
    description="Assemble a final report. The report MUST start with the full scraped article content, followed by the structured analysis (summary, topics, sentiment).",
    expected_output="A complete, well-formatted markdown report containing the full article text and its detailed analysis.",
    agent=report_assembler,
    context=[scrape_task, analysis_task]
)
