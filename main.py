from scrape import scrape_website, split_dom_content, clean_body_content, extract_body_content
from parse import parse_with_ai
from urllib.parse import urlparse
import validators
from selenium.common.exceptions import WebDriverException
import os
import streamlit as st
import streamlit_authenticator as stauth


# st.json(st.user)

if not st.user["is_logged_in"]:
    st.title("AI Web Scraper")
    if st.button("Authenticate with Google to proceed"):
        st.login("google")
else:
    st.image(st.user.picture, width=64)
    st.title(f"{st.user.given_name}'s AI Web Scraper")
    url = st.text_input("Enter a Website URL: ")

    if st.button("Scrape Site"):
        # Validate URL
        if not url:
            st.error("Please enter a website URL.")
        else:
            # Prepend scheme if missing
            parsed_url = urlparse(url)
            if not parsed_url.scheme:
                url_to_scrape = "http://" + url
            else:
                url_to_scrape = url
            # Use validators to check if it's a valid URL
            if not validators.url(url_to_scrape):
                st.error("Invalid URL. Please enter a valid website address (e.g., https://example.com).")
            else:
                try:
                    with st.spinner("Scraping the Website..."):
                        result = scrape_website(url_to_scrape)
                        body_content = extract_body_content(result)
                        cleaned_content = clean_body_content(body_content)
                        st.session_state.dom_content = cleaned_content
                    with st.expander("View DOM Content"):
                        st.text_area("DOM Content", cleaned_content, height=500)
                except WebDriverException as e:
                    st.error("Could not resolve the website address or load the page. Please check the URL and try again.")
                except Exception as e:
                    st.error(f"Failed to scrape the website: {e}")

    if "dom_content" in st.session_state:
        parse_description = st.text_area("What info do you want to retrieve?")

        # Backend selection
        backend = st.selectbox("Choose AI backend", ["openai", "ollama"], format_func=lambda x: "OpenAI (cloud)" if x=="openai" else "Ollama (local)")

        if st.button("Parse Content"):
            with st.spinner("Parsing the content with AI..."):
                dom_chunks = split_dom_content(st.session_state.dom_content)
                try:
                    result = parse_with_ai(dom_chunks, parse_description, backend=backend)
                    st.write(result)
                except Exception as e:
                    st.error("Failed to parse content with AI. Please ensure the selected AI backend is running and the model is available.\nError: {}".format(e))

    st.button("Log out", on_click=st.logout)
