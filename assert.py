import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(link)

first = browser.find_element(By.XPATH, "//div[@class='form-group first_class']/input[contains(@placeholder, 'name')]")
first.send_keys('12')

last = browser.find_element(By.XPATH, "//div[@class='form-group second_class']/input[contains(@placeholder, 'name')]")
last.send_keys('123')

email = browser.find_element(By.XPATH, "//div[@class='form-group third_class']/input[@placeholder= 'Input your email']")
email.send_keys('1234')

button_submit = browser.find_element(By.XPATH, "//button[@type = 'submit']")
button_submit.click()

text = browser.find_element(By.XPATH, "//h1")
txt = text.text
time.sleep(5)
assert txt == "Congratulations! You have successfully registered!"
time.sleep(5)


#делать более точные или менее точные селекторы ебаные
