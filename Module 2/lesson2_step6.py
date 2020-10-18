from selenium import webdriver
import math
import time


def calculate_equation(x):
    res = math.log(abs(12 * math.sin(x)))
    return res

link = "http://suninjuly.github.io/execute_script.html"

browser = webdriver.Chrome()
browser.get(link)

try:
    x = browser.find_element_by_id("input_value").text
    res = calculate_equation(int(x))

    answer_field = browser.find_element_by_id("answer")
    answer_field.send_keys(str(res))

    robotCheckbox = browser.find_element_by_id("robotCheckbox")
    robotCheckbox.click()

    robotsRule = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true)", robotsRule)
    robotsRule.click()

    button = browser.find_element_by_tag_name("button")
    # browser.execute_script("return arguments[0].scrollIntoView(true)", button)
    button.click()
    time.sleep(5)
finally:
    browser.quit()
