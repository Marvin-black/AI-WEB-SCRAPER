import streamlit as st
from scrape import (
    scrape_website,
    split_dom_content,
    clean_body_content,
    extract_body_content,
)
from parse import parse_with_ollama_optimized


st.title("AI WEB SCRAPER")

# Input URL from the user
url = st.text_input("Enter a Website URL: ")

# Scraping the website
if st.button("Scrape site"):
    st.write("Scraping the website...")

    # Perform scraping
    result = scrape_website(url)
    
    # Extract and clean the body content
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)

    # Store cleaned content in session state
    st.session_state.dom_content = cleaned_content

    # Allow users to view the scraped DOM content
    with st.expander("View DOM Content"):
        st.text_area("DOM Content", cleaned_content, height=300)

# Check if DOM content is available for parsing
if "dom_content" in st.session_state:
    # Prompt user for the parsing description
    parse_description = st.text_area("Describe what you want to parse")

    # Parsing the content using the optimized method
    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content...")

            # Split DOM content into chunks for processing
            dom_chunks = split_dom_content(st.session_state.dom_content)

            # Call the optimized parsing function with threaded execution
            result = parse_with_ollama_optimized(dom_chunks, parse_description)

            # Display parsed results
            st.write(result)
