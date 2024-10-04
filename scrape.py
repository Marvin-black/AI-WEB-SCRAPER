import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

def scrape_website(website):
    """
    Launch the Chrome browser, scrape the website content, and return the HTML source.
    Handles the browser lifecycle to ensure it closes properly even on failure.
    """
    print("Launching Chrome browser...")

    # Specify Chrome Driver path and initialize Chrome browser options
    chrome_driver_path = "./chromedriver"
    options = webdriver.ChromeOptions()
    
    # Suppress unnecessary logs and run headless (optional optimization)
    options.add_argument("--headless")
    options.add_argument("--log-level=3")
    
    # Launch the browser with the specified options
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        # Attempt to load the website
        driver.get(website)
        print(f"Page loaded: {website}")

        # Extract the page source after the page is loaded
        html = driver.page_source
        return html
    
    except Exception as e:
        # Log any errors encountered during scraping
        print(f"An error occurred while loading the page: {e}")
        return ""
    
    finally:
        # Ensure the browser is properly closed after operation
        driver.quit()


def extract_body_content(html_content):
    """
    Extract the body content from the HTML using BeautifulSoup.
    """
    soup = BeautifulSoup(html_content, "html.parser")
    
    # Extract the body tag's content
    body_content = soup.body
    
    if body_content:
        return str(body_content)  # Return the body content as a string
    return ""  # Return an empty string if body content is not found


def clean_body_content(body_content):
    """
    Clean the body content by removing all script and style tags.
    Return the cleaned, readable text.
    """
    soup = BeautifulSoup(body_content, "html.parser")
    
    # Remove all script and style elements from the HTML
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    # Get the cleaned text content and strip unnecessary spaces
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )

    return cleaned_content


def split_dom_content(dom_content, max_length=6000):
    """
    Split the cleaned DOM content into chunks of a specified max length.
    This is done to fit into the constraints of the model's input size.
    """
    return [
        dom_content[i: i + max_length] for i in range(0, len(dom_content), max_length)
    ]
