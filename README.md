# AI_web_scrapper_selenium_llama
This project is a Streamlit web application that scrapes website content using Selenium, cleans and processes the data, and then utilizes the Llama 3.2 language model to extract relevant information based on user queries.

### Features:

- Scrapes website content dynamically using `selenium`.
- Cleans extracted content to remove unnecessary elements, reducing token usage.
- Splits content into batches of 25,000 characters to comply with LLM input constraints.
- Passes processed content to Llama 3.2 for answering user queries.

## Installation

### Prerequisites:

- Python 3.8+
- Install dependencies using:
  ```bash
  pip install -r requirements.txt
  ```

## Usage

Run the Streamlit app with:
  ```bash
  streamlit run app.py
```

## Workflow:

1. Enter a website URL in the input field.

2. Click "Scrape Site" to extract and clean content.

3. View the cleaned DOM content.

4. Provide a description of the information you want to extract.

5. Click "Parse content" to process the data with Llama 3.2.

## Modules

### scrape.py

- Uses undetected-chromedriver to fetch and render the webpage.

- Scrolls the page to mimic human behavior.

- Extracts the raw HTML content.

### clean.py

- Removes unnecessary elements like <script>, <style>, <meta>, <link>, and <noscript>.

- Strips out navigation bars, footers, and comments.

- Splits large content into chunks of 25,000 characters.

### parse.py

- Uses langchain_ollama to pass text chunks to Llama 3.2.

- Extracts and formats relevant information based on user input.

## Improvements

-Implementing a tokenizer to count tokens dynamically before sending requests to the LLM.

-Enhancing the extraction process to handle multi-page websites.

- Introducing caching mechanisms for improved efficiency.

## License

MIT License

## Acknowledgement
This project is a derivative work inspired by the excellent tutorial "Python AI Web Scraper Tutorial" by Tech with Tim, available at https://www.youtube.com/watch?v=Oo8-nEuDBkk.

While the core structure of the project is based on Tech with Tim's tutorial, I have made significant modifications, especially regarding the scrapping logic, HTML cleaning and Llama integration.

## Note

To ensure the highest success rate when scraping websites, consider integrating a proxy and captcha solving service like Bright Data, Smart Proxy, or Scraping Ant. These services provide a pool of rotating residential proxies and powerful captcha solvers, which are crucial for bypassing website blocks and CAPTCHAs. While your Selenium-based scraper incorporates headers, mouse scrolling, and timed pauses to mimic human behavior, it will likely encounter limitations.
