🌐 Web Content Scraper Crew 

An LLM-driven **web scraper** built using [crewAI](https://docs.crewai.com), [Hyperbrowser](https://docs.crewai.com/en/tools/web-scraping/hyperbrowserloadtool), and [Ollama](https://ollama.com/). This project scrapes any public webpage, analyzes its content, and outputs a report with summaries, key topics, and sentiment — all handled by autonomous agents.

---

## 🧠 Project Overview

**Agents:**
- `researcher`: Uses Hyperbrowser to scrape full webpage content.
- `analyst`: Summarizes, extracts key points, and determines sentiment.
- `report_assembler`: Combines content and analysis into a markdown report.

**Built with:**
- Python 3.11.8+
- Streamlit UI
- HyperbrowserLoadTool
- Ollama LLM (llama3.2:3b recommended)
- crewAI framework (hierarchical workflow)

---

## 📁 File Structure

```
website-scraper-crew/
├── .env                     # API key for Hyperbrowser
├── agents.py                # Agent definitions with LLM setup
├── app.py                   # Streamlit frontend
├── key_demo.py              # Key loader script (for testing)
├── main.py                  # Task execution + output saving
├── requirements.txt         # Python dependencies
├── tasks.py                 # Task descriptions for agents
```

---

## 🔑 .env

Create a `.env` file to store your Hyperbrowser API key:

```
HYPERBROWSER_API_KEY=your_hyperbrowser_api_key_here
```

---

## 💾 Installation & Setup

1. **Clone the project**:
   ```bash
   git clone https://github.com/yourusername/website-scraper-crew.git
   cd website-scraper-crew
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Pull a suitable Ollama model**:
   Recommended:
   ```bash
   ollama pull llama3:3b
   ```

4. **Start Ollama server (if not already running)**:
   ```bash
   ollama serve
   ```

5. **Add your Hyperbrowser key to `.env`**

---

## 🧪 Run via Terminal

```bash
python main.py
```

Edit `main.py` to provide the target URL inside `run_website_analysis()` or import and call it with a URL of your choice.

---

## 🖥️ Run via Streamlit UI

```bash
streamlit run app.py
```

- Paste the URL in the input box.
- Click "Analyze" to run the agent workflow.
- The markdown report is displayed and saved locally.

---

## 📝 Example Output

Output is saved as:

```
website_scrape_report_2025-07-22_13-50-00.md
```

Contents include:
- Full scraped article
- Summary
- Key topics
- Sentiment in one sentence

---


## ✅ Conclusion

This tool provides an intelligent, modular, and extensible framework for scraping and analyzing web content using modern AI agents. Whether you're an analyst, researcher, or automation enthusiast, the Website Scraper Crew is your plug-and-play solution for structured web intelligence powered by local LLMs and real-time tools.
