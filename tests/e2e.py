import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
flask_url = "http://127.0.0.1:5000"


# Getting element from created URL and checking value
def test_score_service(url):
    driver.get(url)
    time.sleep(3)
    score_element = driver.find_element(By.ID, "score")
    current_score = int(score_element.text)
    if 1000 >+ current_score >= 0:
        return True
    else:
        return False


# Implementing the test for Flask URL and returning 0 if the test passed.
def main_function():
    test = test_score_service(flask_url)
    if test:
        return 0
    else:
        return -1


main_function()
