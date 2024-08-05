import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

link = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()
browser.get(link)

current_dir = os.path.abspath(os.path.dirname(__file__)) # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'TEXT.txt') # добавляем к этому пути имя файла

browser.find_element(By.XPATH, "//div[@class='form-group']/input[@name='firstname']").send_keys('qwe')
browser.find_element(By.XPATH, "//div[@class='form-group']/input[@name='lastname']").send_keys('qwe')
browser.find_element(By.XPATH, "//div[@class='form-group']/input[@name='email']").send_keys('qwe')
browser.find_element(By.XPATH, "//input[@id='file']").send_keys(__file__)
browser.find_element(By.XPATH, "//button").click()

alert = browser.switch_to.alert
alert_text = alert.text
alert.accept()

print(alert_text)
