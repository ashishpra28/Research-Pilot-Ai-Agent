# ResearchPilot - Deep Research AI Agent

ResearchPilot is an AI-powered deep research intelligence system that automates the process of gathering information from the web, extracting relevant content, generating structured research reports, reviewing findings, and refining outputs.

Built using LangChain, Tavily Search, Groq LLMs, BeautifulSoup, and Streamlit.

---

## Features

- Web research using Tavily Search
- Automatic URL extraction
- Web scraping and content extraction
- Structured report generation
- Report review and feedback generation
- Automatic report revision
- Interactive Streamlit dashboard
- Download final research reports

---

## Tech Stack

- Python
- LangChain
- Groq LLM
- Tavily Search API
- BeautifulSoup4
- Streamlit
- UV Package Manager

---

## Project Structure

```text
Research-Pilot/
│
├── app.py
├── requirements.txt
├── pyproject.toml
├── README.md
│
└── modules/
    ├── __init__.py
    ├── agent.py
    ├── tools.py
    ├── prompts.py
    ├── pipeline.py
    └── chat.py
```

---

## Workflow

```text
User Topic
    ↓
Search Agent
    ↓
Web Search
    ↓
URL Extraction
    ↓
Content Scraping
    ↓
Report Generation
    ↓
Report Review
    ↓
Report Revision
    ↓
Final Research Report
```

---

## Run Application

```bash
streamlit run app.py
```

---

## Future Improvements

Make a multi agent system :

- Academic Paper Search Agent
- Fact Checking Agent
- Planner Agent
- Source Reliability Scoring
- PDF Report Export
- Citation Generation
- Advanced Research Workflows
