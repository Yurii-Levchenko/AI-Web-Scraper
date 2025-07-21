# 🕸️ AI Web Scraper

[![Streamlit App](https://img.shields.io/badge/Live%20App-Click%20Here-brightgreen?logo=streamlit)](https://ai-web-scraperrr.streamlit.app/)

**Live Demo:** [https://ai-web-scraperrr.streamlit.app/](https://ai-web-scraperrr.streamlit.app/)

An advanced, cloud-ready web scraping application with a modern Streamlit UI, Google OAuth authentication, and AI-powered content extraction using Selenium and large language models (LLMs).

---

## 🚀 Features

- **Streamlit Web Interface**  
  Intuitive, interactive UI for scraping and parsing any website.

- **Google OAuth Authentication**  
  Secure user login with Google, ready for public or private deployments.

- **Dynamic Content Scraping**  
  Uses Selenium with headless Firefox to handle JavaScript-heavy and dynamic sites.

- **AI-Powered Parsing**  
  Extracts and summarizes web content using LLMs (OpenAI or Ollama).

- **Cloud-Ready**  
  Deployable on Streamlit Community Cloud or any Linux server.

- **Stealth & Anti-Bot**  
  Randomized window size, custom user-agent, and simulated mouse movements to reduce bot detection.

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/) – UI and deployment
- [Selenium](https://www.selenium.dev/) – Browser automation
- [webdriver-manager](https://pypi.org/project/webdriver-manager/) – Automatic driver management
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) – HTML parsing
- [OpenAI](https://platform.openai.com/) / [Ollama](https://ollama.com/) – LLM-based content extraction
- [Google OAuth](https://developers.google.com/identity/protocols/oauth2) – Authentication

---

## ⚡ Quick Start

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/ai-web-scraper.git
   cd ai-web-scraper
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up secrets**
   - Configure Authentication Credentials. Add your `OPENAI_API_KEY` and (optionally) `GITHUB_TOKEN` to `.streamlit/secrets.toml`:
     ```toml
     OPENAI_API_KEY = "sk-..."
     GITHUB_TOKEN = "ghp-..."

     [auth]
     redirect_uri="http://localhost:8501/oauth2callback" # your localhost
     cookie_secret="???" # generate random

     [auth.google]
     client_id="???"
     client_secret="???"
     server_metadata_url="https://accounts.google.com/.well-known/openid-configuration" # depends on your host
     ```

4. **(For cloud) Add Firefox to packages.txt**
   ```
   firefox-esr
   ```

5. **Run the app**
   ```bash
   streamlit run main.py
   ```

---

## 🌐 Deployment

- **Streamlit Community Cloud:**  
  Push to GitHub and deploy directly.

---

## 📝 Usage

1. **Log in with Google**
2. **Enter a website URL** to scrape
3. **Describe what you want to extract** (e.g., "List all main titles in a table")
4. **Choose AI backend** (Currently supported: OpenAI [gpt-4o-mini])
5. **View results**

---

## 🧠 Example Prompts

- "Extract all product names and prices. Form a table of them."
- "Summarize the main news headlines."
- "List all links on the page."

---

## 🛡️ Disclaimer

- Use responsibly. Respect website terms of service and robots.txt.
- Some sites may block scraping from cloud IPs.

---

## 📄 License

MIT License

---

## 🙌 Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Selenium](https://www.selenium.dev/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [OpenAI](https://platform.openai.com/)
- [Ollama](https://ollama.com/)
- [webdriver-manager](https://pypi.org/project/webdriver-manager/)

---

> **Feel free to contact the author**