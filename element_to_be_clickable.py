from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'http://suninjuly.github.io/wait2.html'
browser = webdriver.Chrome()
browser.get(link)

button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//button"))).click()
text = browser.find_element(By.XPATH, "//div[@id = 'verify_message']").text
assert text == "Verification was successful!"

