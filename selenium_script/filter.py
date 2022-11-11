from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions
import streamlit as st


def find_search_bar(driver,search_term):
    try:
        xpath_search = '//input[@aria-label="Search query"]'
        search_input = driver.find_element(By.XPATH ,xpath_search)
        search_input.send_keys(search_term)
        search_input.send_keys(Keys.RETURN)
    #    return None
    except exceptions.TimeoutException:
        return st.error("Timeout while waiting for Login screen", icon="🚨")  

   
def select_tab(driver,tab):
    try:
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, '//div[@data-testid="ScrollSnap-List"]')))
        ScrollSnap_List = driver.find_element(By.XPATH,'//div[@data-testid="ScrollSnap-List"]')
        tab_xpath = f'//div/span[text()= "{tab}"]'
        select_tab = ScrollSnap_List.find_element(By.XPATH,tab_xpath)
        select_tab.click()
        return None
    except exceptions.TimeoutException:
        return st.error("Timeout while waiting for Login screen", icon="🚨")  
