import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'https://suninjuly.github.io/execute_script.html'
browser = webdriver.Chrome()
browser.get(link)

input_value = "//div[@class='form-group']/label/span[@id='input_value']"
answer_space = "//div[@class='form-group']/input[@id='answer']"
check = "//div[@class='form-check form-check-custom']/input[@id='robotCheckbox']"
radio1 = "//div[@class='form-check form-radio-custom']/input[@id='robotsRule']"
submit_button = "//button"

x = browser.find_element(By.XPATH, input_value).text
def calc(x):
    return (math.log(abs(12*math.sin(int(x)))))

answer = browser.find_element(By.XPATH, answer_space).send_keys(calc(x))
check_click = browser.find_element(By.XPATH, check).click()
radio1_click = browser.find_element(By.XPATH, radio1).click()
submit_button_click = browser.find_element(By.XPATH, submit_button).click()
time.sleep(7)
