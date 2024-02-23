from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
import time


options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)


driver.get("https://www.linkedin.com/login")

def login(driver):
    email = driver.find_element(by=By.ID,value="username")
    email.send_keys("")
    pwd = driver.find_element(by=By.ID,value="password")
    pwd.send_keys("")
    submit= driver.find_element(By.CSS_SELECTOR, "button.btn__primary--large")
    submit.click()
    time.sleep(3)
    getProfileURl()


def getProfileURl():
    time.sleep(30)
    finder = driver.find_element(By.CSS_SELECTOR,"search-global-typeahead__input")
    finder.send_keys("Ycombinator")
    search = driver.find_element(By.CSS_SELECTOR,"search-global-typeahead__search-icon-container")
    search.click()




login(driver)
