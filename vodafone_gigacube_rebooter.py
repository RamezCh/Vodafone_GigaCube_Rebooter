import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
ROUTER_IP = "192.168.0.1"
LOGIN_URL = f"http://{ROUTER_IP}/index.html#login"
RESTART_URL = f"http://{ROUTER_IP}/index.html#others"

# Selectors / IDs
PASSWORD_ID = "txtPwd"
LOGIN_BUTTON_ID = "btnLogin"
RESTART_BUTTON_SELECTOR = "input[data-trans='restart_button'][data-bind*='restart']"
RESTART_CONFIRMATION_BUTTON_ID = "yesbtn"

TIMEOUT = 10
INTERNET_TEST_URLS = ["https://www.google.com", "https://www.cloudflare.com"]
INTERNET_TEST_TIMEOUT = 5
REBOOT_WAIT = 60 * 1.5  # seconds to wait after router restart before recheck

# Brave Browser config
BRAVE_PATH = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
# Or The path from chromedriver_installer script (Be sure to download it when you have internet for future usage!)
# If your Browser is updated you need to run chromedriver_installer again and change the path!
CHROMEDRIVER_PATH = r"C:\Users\Your_Username\.wdm\drivers\chromedriver\win64\139.0.7258.138\chromedriver-win32\chromedriver.exe"


def is_internet_up():
    """Check if internet is reachable via multiple URLs"""
    for url in INTERNET_TEST_URLS:
        try:
            requests.get(url, timeout=INTERNET_TEST_TIMEOUT)
            return True
        except requests.RequestException:
            continue
    return False


def wait_and_click(driver, by, selector, pause=2):
    """Wait until element is clickable and click it"""
    WebDriverWait(driver, TIMEOUT).until(
        EC.element_to_be_clickable((by, selector))
    ).click()
    time.sleep(pause)


def restart_router():
    """Restart the router through web interface"""
    driver = None
    try:
        # Configure Brave options
        options = webdriver.ChromeOptions()
        options.binary_location = BRAVE_PATH
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        # Use local chromedriver
        service = Service(CHROMEDRIVER_PATH)
        driver = webdriver.Chrome(service=service, options=options)

        password = os.getenv("ROUTER_PASSWORD")
        if not password:
            raise ValueError("Router password not found in environment variables")

        # Login
        driver.get(LOGIN_URL)
        WebDriverWait(driver, TIMEOUT).until(
            EC.presence_of_element_located((By.ID, PASSWORD_ID))
        ).send_keys(password)
        wait_and_click(driver, By.ID, LOGIN_BUTTON_ID)

        # Navigate and restart
        driver.get(RESTART_URL)
        wait_and_click(driver, By.CSS_SELECTOR, RESTART_BUTTON_SELECTOR)
        wait_and_click(driver, By.ID, RESTART_CONFIRMATION_BUTTON_ID)

        print("Router restart initiated")
        return True

    except Exception as e:
        print(f"Error during router restart: {str(e)}")
        return False

    finally:
        if driver:
            driver.quit()


def main():
    print("Internet connection monitor started...")
    while True:
        print("Checking Internet Connection...")
        if not is_internet_up():
            print("Internet connection down - restarting router...")
            if restart_router():
                print(f"Waiting {REBOOT_WAIT} seconds for router to reboot...")
                time.sleep(REBOOT_WAIT)
            else:
                print(f"Restart failed. Waiting {REBOOT_WAIT} seconds before retry...")
                time.sleep(REBOOT_WAIT)
        else:
            print("Internet connection is active. Exiting.")
            break


if __name__ == "__main__":
    main()