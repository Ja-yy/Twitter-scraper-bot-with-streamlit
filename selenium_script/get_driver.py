from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from fake_headers import Headers
from selenium.webdriver.chrome.options import Options as ChromeOption
from selenium.webdriver.firefox.options import Options as FirfoxOption
import streamlit as st
from selenium import webdriver


def init_driver(headless,browser_name="chrome"):
    def set_properties(browser_option):
        ua = Headers().generate()
        if headless:
            browser_option.add_argument('--headless')
        else:
            pass
        browser_option.add_argument('--incognito')
        browser_option.add_argument("--disable-notifications")
        browser_option.add_argument(f'user-agent={ua}')
        return browser_option

    try:
        browser_name = browser_name.strip().title()
        if browser_name.lower() == "chrome":
            browser_option = ChromeOption()
            browser_option = set_properties(browser_option=browser_option)
            browser_option.add_experimental_option("detach", True)
            driver = webdriver.Chrome(ChromeDriverManager().install(),options=browser_option)
        elif browser_name.lower() == "firefox":
            browser_option = FirfoxOption()
            browser_option = set_properties(browser_option=browser_option)
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),options=browser_option)
        else:
            return st.error("Brower Not supported!")
        return driver

    except Exception as ex:
        return ex

   
def redirect(browser_name="chrome",headless=False):
    URL = "https://twitter.com/login"

    driver = init_driver(headless,browser_name)
    try:
        driver.get(URL)
        return driver
    except AttributeError:
        return ("Driver is not set")

