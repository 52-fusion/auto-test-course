import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = 'http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome()
browser.get(link)

browser.find_element(By.XPATH, "//button").click()

confirm = browser.switch_to.alert
confirm.accept()
x = browser.find_element(By.XPATH, "//span[@id='input_value']").text

def calc(x):
    return (math.log(abs(12*math.sin(int(x)))))

browser.find_element(By.XPATH, "//input[@id='answer']").send_keys(calc(x))

browser.find_element(By.XPATH, "//button").click()

alert = browser.switch_to.alert
alert_text = alert.text
alert.accept()

print(alert_text)
