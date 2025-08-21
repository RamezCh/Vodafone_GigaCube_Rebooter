"""
Chrome WebDriver Example with Auto-Download

This script uses Selenium and webdriver-manager to automatically
download the correct version of ChromeDriver and open Google's homepage.
Ideal for automation, testing, or web scraping projects.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def create_chrome_driver(headless=False):
    """
    Creates and returns a configured Chrome WebDriver instance.

    Args:
        headless (bool): If True, runs Chrome in headless mode (no GUI).

    Returns:
        webdriver.Chrome: Configured Chrome driver.
    """
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless")

    # Recommended arguments to improve stability
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    # Automatically downloads and sets up chromedriver
    driver_path = ChromeDriverManager().install()
    print(f"ChromeDriver path: {driver_path}")
    service = Service(driver_path)

    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver


def main():
    """Main function to run the automation."""
    driver = None
    try:
        driver = create_chrome_driver(headless=False)  # Set to True for headless
        driver.get("https://www.google.com")
        print("Page title:", driver.title)
    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        if driver:
            driver.quit()
            print("Browser closed.")

# This downloads the driver, you can either use it in vodafone_gigacube_rebooter from cache or move it into specified path for future re-usability
if __name__ == "__main__":
    main()