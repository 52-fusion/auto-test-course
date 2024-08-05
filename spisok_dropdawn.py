import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

num1 = browser.find_element(By.XPATH, "//span[@id = 'num1']").text
num2 = browser.find_element(By.XPATH, "//span[@id = 'num2']").text

summa = (int(num1) + int(num2))

dropdow = browser.find_element(By.XPATH, "//select").click()
dropdown_value = browser.find_element(By.XPATH, f"//select/option[@value={str(summa)}]").click()

submit = browser.find_element(By.XPATH, "//button").click()
time.sleep(7)
#опционально
'''
from selenium.webdriver.support.ui import Select
select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value("1") # ищем элемент с текстом "Python"

Можно использовать еще два метода: select.select_by_visible_text("text") и select.select_by_index(index).
Первый способ ищет элемент по видимому тексту, например, select.select_by_visible_text("Python") найдёт "Python"
для нашего примера.

Второй способ ищет элемент по его индексу или порядковому номеру.
Индексация начинается с нуля. Для того чтобы найти элемент с текстом "Python", нужно
использовать select.select_by_index(1), так как опция с индексом 0 в данном примере
имеет значение по умолчанию равное "--".
'''
