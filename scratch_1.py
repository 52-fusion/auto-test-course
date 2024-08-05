'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://www.google.com/"
browser = webdriver.Chrome()
time.sleep(2)
browser.get(link)
time.sleep(2)
path_button = '//textarea[@class="gLFyf"]'
button = browser.find_element(By.XPATH, path_button)
time.sleep(2)
button.send_keys("HUILA")
time.sleep(3)
'''


'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"
browser = webdriver.Chrome()

time.sleep(5)
browser.get(link)
time.sleep(1)
button = browser.find_element(By.ID, "submit_button")
button.click()
time.sleep(5)
'''
