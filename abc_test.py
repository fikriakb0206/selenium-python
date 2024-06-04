from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
import softest
import pytest

Options = Options()
Options.add_experimental_option("detach", True)



@pytest.fixture
def driver():
    driver = webdriver.Chrome(options=Options)
    driver.maximize_window()
    driver.get("https://trial.rpl.id/landing/index.html")
    home = driver.implicitly_wait(5)
    home = driver.find_element(By.CSS_SELECTOR, 'button.xbutton')
    home.click()
    yield driver
    
def test_home(driver):    
    login = driver.find_element(By.XPATH, '//a[@href="/login"]')
    login.click()
    login = driver.find_element(By.XPATH, '//input[@name="email"]').send_keys ('rplkeysuper@gmail.com')
    login = driver.find_element(By.XPATH, '//input[@name="password"]').send_keys ('RPLsuper2023!')
    login = driver.find_element(By.XPATH, '//button[@type="submit"]')
    login.click()

# def login(driver):
