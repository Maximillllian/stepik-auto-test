from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = 'http://suninjuly.github.io/selects2.html'

browser = webdriver.Chrome()
browser.get(link)

num1 = browser.find_element_by_id("num1").text
num2 = browser.find_element_by_id("num2").text
sum_ = int(num1) + int(num2)

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(str(sum_))

button = browser.find_element_by_tag_name("button")
button.click()

time.sleep(10)
browser.quit()
