from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()
browser.get(link)

# Работа с выпадающими списками обычным способом
browser.find_element_by_tag_name("select").click()
browser.find_element_by_css_selector("[value='1']").click()
time.sleep(3)

# Можно иницализировать выпадающий список с помощью класса Select
select = Select(browser.find_element_by_tag_name("select"))

# И уже в этом классе выбирать нужный вариант
select.select_by_value("49")

# Есть еще два метода: select.select_by_visible_text("text") и select.select_by_index(index)
# Первый ищет по видимому для польщователя тексту, второй по индексу (порядковому номеру среди других вариантов)

time.sleep(5)
browser.quit()