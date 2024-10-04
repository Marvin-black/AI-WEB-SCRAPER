from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from concurrent.futures import ThreadPoolExecutor, as_completed

# Define the template
template = (
    "You are tasked with extracting precise information from the following text content: {dom_content}. "
    "Please adhere strictly to the following guidelines: \n\n"
    "1. **Targeted Extraction:** Only extract the information that strictly matches the provided description: {parse_description}. "
    "Ensure that the extracted data aligns exactly with the requested parameters, without including surrounding or unrelated details.\n\n"
    "2. **No Additional Content:** Do not include any extra text, comments, explanations, or formatting in your response. "
    "Your output should be concise and limited to the requested information only.\n\n"
    "3. **Return Empty String If Not Found:** If the requested information cannot be found, or if it does not match the description, "
    "return an empty string (`''`) without providing any justifications or alternative data.\n\n"
    
)

model = OllamaLLM(model="llama3.1")

# Function to process a single DOM chunk
def process_chunk(chunk, parse_description, chain):
    return chain.invoke({"dom_content": chunk, "parse_description": parse_description})

# Main function to parse DOM chunks with optimized performance
def parse_with_ollama_optimized(dom_chunks, parse_description, max_workers=4):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    parsed_results = []
    # Use ThreadPoolExecutor to parallelize the processing of chunks
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_chunk = {executor.submit(process_chunk, chunk, parse_description, chain): chunk for chunk in dom_chunks}

        for i, future in enumerate(as_completed(future_to_chunk), start=1):
            try:
                response = future.result()
                parsed_results.append(response)
                print(f"Parsed batch: {i} of {len(dom_chunks)}")
            except Exception as e:
                print(f"Error processing chunk: {e}")

    return "\n".join(parsed_results)
