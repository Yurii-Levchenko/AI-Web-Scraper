import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import random
from selenium.webdriver.common.action_chains import ActionChains

def scrape_website(website):
    print("Launching chrome browser...")

    chrome_driver_path = "chromedriver.exe"
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # run Chrome in headless mode
    options.add_argument("--disable-gpu")  # optional: disables GPU hardware acceleration
    options.add_argument("--no-sandbox")  # optional: required for some Linux environments
    options.add_argument("--lang=en-US,en")
    # Set a custom user-agent to avoid basic bot detection
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    options.add_argument(f"--user-agent={user_agent}")
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    # Randomize window size to avoid obvious automation
    width = random.randint(1200, 1920)
    height = random.randint(700, 1080)
    driver.set_window_size(width, height)
    print(f"Set window size to {width}x{height}")

    try:
        driver.get(website)
        print("page loaded...")
        try:
            # Wait for the <body> tag to be present (dynamic content)
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            print("Body tag loaded.")
        except TimeoutException:
            print("Timed out waiting for page to load <body> tag.")

        # Simulate mouse movements and scrolling
        actions = ActionChains(driver)
        for _ in range(random.randint(2, 4)):
            x = random.randint(0, width-1)
            y = random.randint(0, height-1)
            print(f"Moving mouse to ({x}, {y})")
            actions.move_by_offset(x, y).perform()
            actions.reset_actions()
            time.sleep(random.uniform(0.2, 0.6))
        # Scroll down a random amount
        scroll_amount = random.randint(100, height//2)
        print(f"Scrolling down by {scroll_amount} pixels")
        driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
        time.sleep(random.uniform(0.5, 1.2))

        html = driver.page_source
        time.sleep(2)  # Shorten sleep, since we now wait for content

        return html
    finally:
        driver.quit()

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

# getting rid of scripts and styles
def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )

    return cleaned_content

# splitting by batches to keep withing LLM's size limit for request
def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i: i + max_length] for i in range(0, len(dom_content), max_length)
    ]