from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

link = 'http://suninjuly.github.io/explicit_wait2.html'
browser = webdriver.Chrome()
browser.get(link)

button1 = browser.find_element(By.XPATH, "//button[@id = 'book']")
WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.XPATH, "//h5[@id='price']"), '$100'))
button1.click()

button2 = browser.find_element(By.XPATH, "//button[@id='solve']")
browser.execute_script("return arguments[0].scrollIntoView(true);", button2)

def calc(x):
    return (math.log(abs(12*math.sin(int(x)))))

x = browser.find_element(By.XPATH, "//span[@id='input_value']").text

browser.find_element(By.XPATH, "//input[@id='answer']").send_keys(calc(x))
button2.click()

alert = browser.switch_to.alert
alert_text = alert.text
alert.accept()

print(alert_text)
