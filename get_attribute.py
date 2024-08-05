import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/get_attribute.html'
browser = webdriver.Chrome()
browser.get(link)

x = browser.find_element(By.XPATH, "//h2/img[@id='treasure']").get_attribute("valuex")
def calc(x):
    return (math.log(abs(12*math.sin(int(x)))))

answer = browser.find_element(By.XPATH, "//div/input[@id='answer']").send_keys(calc(x))
check = browser.find_element(By.XPATH, "//div/input[@id='robotCheckbox']").click()
radio = browser.find_element(By.XPATH, "//div/input[@id='robotsRule']").click()
submit = browser.find_element(By.XPATH, "//div/button[@type = 'submit']").click()

time.sleep(7)
