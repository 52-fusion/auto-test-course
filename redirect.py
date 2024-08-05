import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()
browser.get(link)

browser.find_element(By.XPATH, "//button").click()


first_window = browser.window_handles[0]
second_window = browser.window_handles[1]
browser.switch_to.window(second_window)

def calc(x):
    return (math.log(abs(12*math.sin(int(x)))))

x = browser.find_element(By.XPATH, "//span[@id = 'input_value']").text
browser.find_element(By.XPATH, "//input[@id = 'answer']").send_keys(calc(x))
browser.find_element(By.XPATH, "//button").click()

alert = browser.switch_to.alert
aler_text = alert.text
alert.accept()

print(aler_text)
