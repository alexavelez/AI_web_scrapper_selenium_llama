from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

prompt_template = """
You are tasked with extracting specific information from the following text content that comes from a scrapped website: 
{dom_content}

**Instructions:**

- **Batch Processing Context:** This data is being processed in multiple batches. Maintain consistent formatting and structure across all batches for easier merging. Do not repeat headers or introductory text unless absolutely necessary.
- **Extract Information:** Only extract the information that directly matches the provided description: {user_input}.
- **No Extra Content:** Do not include additional text, comments, or explanations in your response unless specifically requested.
- **Consistent Formatting:** Ensure that the format (e.g., table, list) remains the same across all batches, even if some batches contain no relevant information.
- **Empty Response:** If no information matches the description in this batch, return an empty string ('').
- **Direct Data Only:** Your output should contain only the data that is explicitly requested, formatted consistently.
- **Output:** 
"""

model = OllamaLLM(model="llama3.2")

def parse_with_ollama(dom_chunks, user_input):

    # Create the ChatPromptTemplate object
    prompt = ChatPromptTemplate.from_template(prompt_template)
    chain = prompt | model

    parsed_results = []

    for i, chunk in enumerate(dom_chunks, start=1):
        response = chain.invoke(
            {"dom_content": chunk, "user_input": user_input}
        )
        print(f"Parsed batch: {i} of {len(dom_chunks)}")
        parsed_results.append(response)

    return "\n".join(parsed_results)