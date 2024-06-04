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
# login
    driver = webdriver.Chrome(options=Options)
    driver.maximize_window()
    driver.get("https://trial.rpl.id/landing/index.html")
    home = driver.implicitly_wait(5)
    home = driver.find_element(By.CSS_SELECTOR, 'button.xbutton')
    home.click()
    login = driver.find_element(By.XPATH, '//a[@href="/login"]')
    login.click()
    login = driver.find_element(By.XPATH, '//input[@name="email"]').send_keys ('rplkeysuper@gmail.com')
    login = driver.find_element(By.XPATH, '//input[@name="password"]').send_keys ('RPLsuper2023!')
    login = driver.find_element(By.XPATH, '//button[@type="submit"]')
    login.click()
    yield driver
    
# def test_create_contact_personal(driver):
#     contact = driver.find_element(By.XPATH, '//a[@href="/dashboard/sales-contact"]').click()
#     contact = driver.find_element(By.XPATH, '//img[@src="/assets/icons/plus-white.svg"]').click()
#     # form input
#     name = "susi p"
#     email = "susi@susider.com"
#     job_posision = "operational"
#     phone = "085477731268"

#     contact = driver.find_element(By.CSS_SELECTOR, 'input#name').send_keys(name)
#     contact = driver.find_element(By.CSS_SELECTOR, 'input#email').send_keys(email)
#     contact = driver.find_element(By.CSS_SELECTOR, 'input#job_position').send_keys(job_posision)
#     contact = driver.find_element(By.CSS_SELECTOR, 'input#phone').send_keys(phone)
#     contact = driver.find_element(By.XPATH, '//input[@name="contact_type"]').click()
#     contact = driver.find_element(By.XPATH, '//ul/li[1]').click()
#     contact = driver.find_element(By.XPATH, '//input[@name="source"]').click()
#     contact = driver.find_element(By.XPATH, '//ul/li[2]').click()
#     contact = driver.find_element(By.XPATH, '//input[@name="contact_status"]').click
#     contact = driver.find_element(By.XPATH, '//ul/li[2]').click() 
#     contact = driver.find_element(By.XPATH, '//button[@type="submit"]').click()
#     contact = driver.implicitly_wait(2)
#     contact = driver.find_element(By.CSS_SELECTOR, 'button.swal2-close').click()
    
def test_create_contact_corporate(driver):
    contact = driver.find_element(By.XPATH, '//a[@href="/dashboard/sales-contact"]').click()
    contact = driver.find_element(By.XPATH, '//img[@src="/assets/icons/plus-white.svg"]').click()
    # form input
    name = "Jahrun"
    email = "jahrun@susider.com"
    job_posision = "operational"
    phone = "0854732455"
    contact = driver.find_element(By.CSS_SELECTOR, 'input#name').send_keys(name)
    contact = driver.find_element(By.XPATH, '//input[@name="source"]').click()
    contact = driver.find_element(By.XPATH, '//ul/li[2]').click()
    contact = driver.find_element(By.CSS_SELECTOR, 'input#email').send_keys(email)
    contact = driver.find_element(By.CSS_SELECTOR, 'input#job_position').send_keys(job_posision)
    contact = driver.find_element(By.CSS_SELECTOR, 'input#phone').send_keys(phone)
    contact = driver.find_element(By.XPATH, '//input[@name="contact_type"]').click()
    contact = driver.find_element(By.XPATH, '//ul/li[2]').click()
    contact = driver.find_element(By.XPATH, '//div[contains(text(),"Select Company")]').click()
    contact = driver.find_element(By.XPATH, '//div[contains(text(),"PT ABCD")]').click()
    contact = driver.find_element(By.XPATH, '//input[@name="contact_status"]').click()
    contact = driver.find_element(By.XPATH, '//ul/li[2]').click() 
    # contact = driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    # contact = driver.implicitly_wait(2)
    # contact = driver.find_element(By.CSS_SELECTOR, 'button.swal2-close').click()

    
    # driver.quit()

