'''button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

browser.execute_script("window.scrollBy(0, 100);")'''
from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.execute_script("alert('Robots at work');")
time.sleep(30)
