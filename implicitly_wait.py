from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/wait1.html'
browser = webdriver.Chrome()
browser.get(link)
browser.implicitly_wait(5) # говорим WebDriver искать каждый элемент в течение 5 секунд

browser.find_element(By.XPATH, "//button").click()
text = browser.find_element(By.XPATH, "//div[@id = 'verify_message']").text
assert text == "Verification was successful!"
