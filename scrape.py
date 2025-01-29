
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import random

chromedriver_path = "./chromedriver"

def get_page_source(url, wait_time=10, element_locator=(By.CSS_SELECTOR, "body")):
    driver = None  # Initialize driver to avoid UnboundLocalError
    try:
        # Set Chrome options
        options = uc.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument(
            'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        )

        # Initialize driver
        driver = uc.Chrome(options=options, use_subprocess=False)

        # Hide webdriver property
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
            Object.defineProperty(navigator, 'webdriver', {
              get: () => undefined
            })
            """
        })

        # Open URL
        driver.get(url)

        # Scroll randomly to mimic human behavior
        for _ in range(random.randint(1, 3)):
            driver.execute_script("window.scrollBy(0, document.body.scrollHeight/3);")
            time.sleep(random.uniform(1, 2))

        # Wait for the element to load
        WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located(element_locator)
        )

        # Return page source
        return driver.page_source

    except Exception as e:
        print(f"Error fetching page source for {url}: {e}")
        return None

    finally:
        if driver:  # Quit driver if it was initialized
            driver.quit()

# Ensure safe entry point for multiprocessing
if __name__ == '__main__':
    url = "https://www.hapag-lloyd.com/en/home.html"
    html = get_page_source(url)
    if html:
        print("Page source fetched successfully!")
