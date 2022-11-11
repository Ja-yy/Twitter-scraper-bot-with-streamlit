from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions
import streamlit as st

def get_id_password(driver,email,password):
    try:
        URL = "https://twitter.com/login"
        driver.get(URL)
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.NAME, 'text')))
        email_filed = driver.find_element(By.NAME ,'text')
        email_filed.send_keys(email)
        email_filed.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.NAME, 'password')))
        password_filed = driver.find_element(By.NAME ,'password')
        password_filed.send_keys(password)
        password_filed.send_keys(Keys.RETURN)
        url = "https://twitter.com/home"
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(url))
        return driver
    except exceptions.TimeoutException:
        st.error("Timeout while waiting for Login screen", icon="🚨")  

   