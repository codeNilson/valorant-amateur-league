import os
from selenium import webdriver
from dotenv import load_dotenv

load_dotenv()


def get_browser(*args):
    options = webdriver.ChromeOptions()
    for arg in args:
        options.add_argument(arg)
    if os.environ.get("SELENIUM_HEADLESS") in ["True", "true", "1"]:
        options.add_argument("--headless")
    return webdriver.Chrome(options=options)


if __name__ == "__main__":
    browser = get_browser()
    browser.get("https://www.google.com")
    browser.quit()
