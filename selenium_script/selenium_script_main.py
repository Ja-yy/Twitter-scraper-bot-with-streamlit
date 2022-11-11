from selenium_script.scroll import scroll_down_page
from selenium_script.filter import find_search_bar,select_tab
from selenium_script.login import get_id_password 
from selenium_script.scrap_handler import collect_all_tweets_from_current_view,extract_data_from_current_tweet_card,generate_tweet_id

from selenium.common import exceptions


def sc_main(driver,username, password, search_term,tab,max_scroll):
    last_position = None
    end_of_scroll_region = False
    unique_tweets = set()

    logged_in = get_id_password(email=username,password=password,driver=driver)

    if not logged_in:
        return 

    search_found = find_search_bar(search_term=search_term,driver= driver)
    select_tab(driver=driver,tab=tab)
    si=0
    while not end_of_scroll_region:
        cards = collect_all_tweets_from_current_view(driver)
        for card in cards:
            try:
                tweet = extract_data_from_current_tweet_card(card)
            except exceptions.StaleElementReferenceException:
                continue
            if not tweet:
                continue
            tweet_id = generate_tweet_id(tweet)
            if tweet_id not in unique_tweets:
                unique_tweets.add(tweet_id)
        si += 1 
        if si <= max_scroll:
            last_position, end_of_scroll_region = scroll_down_page(driver, last_position)
        else:
            end_of_scroll_region = True

    # driver.quit()
    return None