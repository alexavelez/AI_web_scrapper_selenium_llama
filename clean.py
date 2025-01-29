from bs4 import BeautifulSoup
from bs4.element import Comment

def extract_cleaned_content(html_content):
    """
    Extracts and cleans the textual content from an HTML document, removing irrelevant 
    elements such as scripts, styles, navigation bars, footers, and comments to focus 
    on the meaningful content.

    Args:
        html_content (str): The raw HTML content of a webpage or document.

    Returns:
        str: A cleaned and formatted string containing the main textual content of the 
             webpage, suitable for further processing or summarization.

    Functionality:
        - Parses the HTML content using BeautifulSoup.
        - Removes irrelevant tags (`<script>`, `<style>`, `<meta>`, `<link>`, and `<noscript>`).
        - Optionally removes `<nav>` and `<footer>` tags to exclude navigation and footer 
          content if they are present.
        - Eliminates all HTML comments to avoid unnecessary noise.
        - Extracts the text from the `<body>` tag if available, or the entire document 
          otherwise.
        - Further cleans the extracted text by:
            - Stripping leading and trailing whitespace.
            - Removing blank lines.
            - Ensuring a consistent and compact text format.

    Importance:
        - Webpages often contain a mix of meaningful content and extraneous code or 
          decorative elements. This function isolates the relevant content, reducing 
          unnecessary tokens for downstream processing (e.g., summarization with LLMs).
        - Helps ensure that the processed content is concise and relevant, improving 
          the efficiency of token usage and the quality of model outputs.

    Example:
        raw_html = "<html><body><p>Hello, world!</p><script>console.log('Hi');</script></body></html>"
        cleaned_content = extract_cleaned_content(raw_html)
        print(cleaned_content)
        # Output: "Hello, world!"
    """
    soup = BeautifulSoup(html_content, "html.parser")
    
    # Remove script, style, and other irrelevant tags
    for tag in soup(["script", "style", "meta", "link", "noscript"]):
        tag.decompose()  # Completely removes the tag and its content
    
    # Optionally remove navigation and footer if they are identifiable
    for tag in soup.find_all(["nav", "footer"]):
        tag.decompose()
    
    # Remove comments
    comments = soup.find_all(string=lambda text: isinstance(text, Comment))
    for comment in comments:
        comment.extract()
    
    # Extract text from the body or the entire document if body is missing
    body_content = soup.body
    if body_content:
        cleaned_content = body_content.get_text(separator=" ", strip=True)
    else:
        cleaned_content = soup.get_text(separator=" ", strip=True)
    
    # Further clean and format the extracted text
    cleaned_content = "\n".join(line.strip() for line in cleaned_content.splitlines() if line.strip())
    
    return cleaned_content


def split_dom_content(dom_content, max_length=25000):
    """
    Splits a long string of content into smaller chunks to ensure compatibility with 
    large language models (LLMs) that have token limits.

    Args:
        dom_content (str): The cleaned HTML content or any long text string that needs 
                           to be processed.
        max_length (int): The maximum length of each chunk in characters. This value 
                          should be chosen based on the average token limit of the LLM 
                          being used (e.g., GPT-4's token limit of 8,000 or 32,000).

    Returns:
        list of str: A list of string chunks, each with a length up to `max_length` 
                     characters, split from the input content.

    Importance:
        - Many LLMs have a limit on the number of tokens they can process in a single 
          input. If the content exceeds this limit, the model will either truncate it 
          or reject the input entirely.
        - This function ensures that large content, such as long web pages, can be 
          divided into manageable chunks that fit within the LLM's constraints.
        - By splitting the content, you can process each chunk independently, allowing 
          for summarization or other tasks without losing data.

    Example:
        cleaned_content = "A very long string of text..."
        chunks = split_dom_content(cleaned_content, max_length=6000)
        for idx, chunk in enumerate(chunks):
            print(f"Chunk {idx + 1}: {chunk[:50]}...")
    """
    return [dom_content[i:i + max_length] for i in range(0, len(dom_content), max_length)]
