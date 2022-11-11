from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common import exceptions


def collect_all_tweets_from_current_view(driver, lookback_limit=25):
    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, '//div[@aria-label="Timeline: Search timeline"]')))
    page_tab = driver.find_element(By.XPATH, '//div[@data-testid="primaryColumn"]')
    # WebDriverWait(driver, 20).until(expected_conditions.presence_of_element_located((By.XPATH, '//div[@data-testid="UserCell"]')))
    page_cards = page_tab.find_elements(By.XPATH, '//div[@data-testid="cellInnerDiv"]')
    if len(page_cards) <= lookback_limit:
        return page_cards
    else:
        return page_cards[-lookback_limit:]


def extract_data_from_current_tweet_card(card):
    try:
        user = card.find_element(By.XPATH,'.//span').text
    except exceptions.NoSuchElementException:
        user = ""
    except exceptions.StaleElementReferenceException:
        return
    try:
        url=""
        handle = card.find_element(By.XPATH,'.//span[contains(text(), "@")]').text
        url = "https://twitter.com/" + handle.replace("@","")
    except exceptions.NoSuchElementException:
        handle = ""
    tweet = (user, handle,url)
    return tweet

def generate_tweet_id(tweet):
    return ''.join(tweet)


