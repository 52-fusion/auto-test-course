import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/huge_form.html"
browser = webdriver.Chrome()
browser.get(link)

pole = "//input[@type = 'text']"
elements = browser.find_elements(By.XPATH, pole)
for element in elements:
    element.send_keys('hiu')

button = browser.find_element(By.XPATH, "//button[@type = 'submit']")
time.sleep(5)
button.click()
time.sleep(5)
