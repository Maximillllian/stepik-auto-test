from selenium import webdriver
from lesson1_step5 import calculate_equation
import time

link = "http://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome()
browser.get(link)

x_value = browser.find_element_by_id("treasure")
x = int(x_value.get_attribute('valuex'))
answer = calculate_equation(x)

answer_field = browser.find_element_by_css_selector("input#answer")
answer_field.send_keys(str(answer))

robot_checkbox = browser.find_element_by_css_selector("input#robotCheckbox")
robot_checkbox.click()

robots_rule = browser.find_element_by_css_selector("input#robotsRule")
robots_rule.click()

button = browser.find_element_by_css_selector("button[type='submit']")
button.click()

time.sleep(10)
browser.quit()