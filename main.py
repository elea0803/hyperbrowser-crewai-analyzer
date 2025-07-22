from dotenv import load_dotenv
from crewai import Crew, Process
from tasks import scrape_task, analysis_task, report_task
from agents import researcher, analyst, report_assembler
from datetime import datetime
from tool import hyperbrowser_tool

load_dotenv()

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

def run_website_analysis(url: str):
    if not url:
        raise ValueError("URL must be provided for website analysis.")
    crew = Crew(
        agents=[researcher, analyst, report_assembler],
        tasks=[scrape_task, analysis_task, report_task],
        process=Process.sequential,
        verbose=True
    )
    try:
        result = crew.kickoff(inputs={'url': url})
    except Exception as e:
        print(f"Crew execution error: {e}")
        raise

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = f"website_analysis_report_{timestamp}.md"
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(str(result))
        print(f"Report successfully saved to {output_file}")
    except Exception as e:
        print(f"Failed to save report to file: {e}")
    return result
