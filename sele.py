from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

browser = webdriver.Chrome(options=options)


browser.get("https://www.google.com")
browser.find_element("id","L2AGLb").click()

m = browser.find_element("name", "q")
m.send_keys("facebook")
time.sleep(0.2)
m.send_keys(Keys.ENTER)

browser.find_element(By.PARTIAL_LINK_TEXT, 'log in or sign up').click()
time.sleep(0.2)

browser.find_element(By.XPATH, '//button[text()="Allow essential and optional cookies"]').click()
email = browser.find_element("name", "email")
email.send_keys("my3mail3xists@something.com")

passw = browser.find_element("name", "pass")
passw.send_keys("aasdjj8j38rj8jv83j9jf39fj39jf93")
time.sleep(0.2)
browser.find_element(By.PARTIAL_LINK_TEXT, 'og in').click()
