import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_link_text"
browser = webdriver.Chrome()
browser.get(link)

number = str(math.ceil(math.pow(math.pi, math.e)*10000))
L_N = f"//a[text() = '{number}']"
print(L_N)
link_num = browser.find_element(By.XPATH, L_N)
link_num.click()

first_name = "//input[@name='first_name']"
last_name = "//input[@name='last_name']"
city = "//input[contains(@class, 'city')]"
country = "//input[@id='country']"
submit = "//button[@type='submit']"

el_FN = browser.find_element(By.XPATH, first_name)
el_FN.send_keys('Ivan')

el_LN = browser.find_element(By.XPATH, last_name)
el_LN.send_keys('Petrov')

el_C = browser.find_element(By.XPATH, city)
el_C.send_keys('Smolensk')

el_CY = browser.find_element(By.XPATH, country)
el_CY.send_keys('Petrov')

button_submit = browser.find_element(By.XPATH, submit)
button_submit.click()


time.sleep(30)
