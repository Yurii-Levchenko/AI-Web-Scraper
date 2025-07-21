AI-powered web scraper with a Streamlit UI, using Selenium for scraping, BeautifulSoup for parsing, and LangChain + Ollama for LLM-based extraction.

Architecture Overview
Frontend/UI: Streamlit app for user interaction.
Scraping: Selenium (with ChromeDriver) to fetch page source.
Parsing: BeautifulSoup to extract and clean the body content.
AI Extraction: LangChain with Ollama LLM to process and extract info based on user prompt.

Workflow:
User enters URL →
Scrape site →
Show DOM content →
User enters parse prompt →
LLM processes and returns result.