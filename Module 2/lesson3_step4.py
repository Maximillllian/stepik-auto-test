from selenium import webdriver
from functions import calculate_equation, find_x, get_alert_answer
import time
from pyperclip import copy

link = 'http://suninjuly.github.io/alert_accept.html'

browser = webdriver.Chrome()
browser.get(link)

try:
    button = browser.find_element_by_tag_name("button")
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

    x = find_x(browser)
    answer_x = calculate_equation(x)

    answer_field = browser.find_element_by_id("answer")
    answer_field.send_keys(str(answer_x))

    submit_button = browser.find_element_by_tag_name("button")
    submit_button.click()

    answer_alert = browser.switch_to.alert
    answer = answer_alert.text.split()[-1]
    copy(answer)

finally:
    browser.quit()