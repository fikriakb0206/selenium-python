from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import softest
import pytest
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://trial.rpl.id/landing/index.html")
    home = WebDriverWait(driver, 2)
    home = driver.find_element(By.CSS_SELECTOR, 'button.xbutton').click()
#     yield driver

# def login(driver):
