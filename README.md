# AI Web Scraper

An AI-powered web scraper built using Selenium, BeautifulSoup, and LangChain's Ollama model, integrated with Streamlit for a user-friendly interface. This project allows users to scrape websites, clean and extract the relevant body content, and perform AI-assisted parsing using the Llama model. It provides an optimized and multi-threaded parsing mechanism to ensure efficient data extraction from large websites.

## Features

- **Web Scraping**: Scrapes website content using Selenium.
- **Body Content Extraction**: Extracts the relevant content from the HTML body using BeautifulSoup.
- **Content Cleaning**: Removes unnecessary script and style tags from the scraped content.
- **AI-Powered Parsing**: Utilizes LangChain's Ollama model for precise and targeted data extraction based on user queries.
- **Multi-threaded Parsing**: Optimized parsing using multi-threading for faster performance.
- **Streamlit Interface**: Provides a simple and intuitive UI for interacting with the scraper and viewing results.

## Technologies Used

- **Selenium**: For web scraping and browser automation.
- **BeautifulSoup**: For parsing and cleaning HTML content.
- **LangChain (Ollama Llama Model)**: For AI-powered content extraction.
- **Streamlit**: For the frontend UI to interact with the web scraper.
- **Python**: Core programming language used in the project.

## How It Works

1. **Enter URL**: Input the website URL you want to scrape.
2. **Scrape Website**: The scraper uses Selenium to retrieve the HTML content of the website.
3. **View and Clean Content**: The body content is extracted and cleaned of unnecessary elements.
4. **Define Parsing Query**: Describe what information you want to parse from the content.
5. **AI Parsing**: The content is split into manageable chunks and passed through the Llama model to extract the desired information.
6. **View Results**: The extracted information is displayed in the Streamlit interface.

## Project Structure

```bash
├── main.py           # Streamlit interface for the web scraper and AI parser
├── parse.py          # Parsing functions using LangChain Ollama model with threading optimization
├── scrape.py         # Scraping and cleaning logic using Selenium and BeautifulSoup
├── requirements.txt  # Required Python packages
└── README.md         # Project documentation
