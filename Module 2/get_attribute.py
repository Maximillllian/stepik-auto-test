from selenium import webdriver
import time

link = "http://suninjuly.github.io/math.html"

browser = webdriver.Chrome()
browser.get(link)
people_radio = browser.find_element_by_id("peopleRule")

# С помощью аттрибута get_attribute мы смотрим значение этого аттрибута в тэге. Если true - значит этот аттрибут включен
# (присутсвует), если false - он не указан в тэге
people_checked = people_radio.get_attribute("checked")
print("value of people radio: ", people_checked)
assert people_checked is not None, "People radio is not selected by default"

robots_radio = browser.find_element_by_id("robotsRule")
robots_checked = robots_radio.get_attribute("checked")
assert robots_checked is None

browser.quit()