from selenium import webdriver
import time
import math


def calculate_equation(x):
    res = math.log(abs(12 * math.sin(x)))
    return res


def input_values(link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        x_value = browser.find_element_by_css_selector("span#input_value")
        x = int(x_value.text)
        answer = calculate_equation(x)
        answer_field = browser.find_element_by_css_selector("input#answer.form-control")
        answer_field.send_keys(str(answer))
        robot_checkbox = browser.find_element_by_css_selector("input#robotCheckbox")
        robot_checkbox.click()
        robots_rule = browser.find_element_by_css_selector("input#robotsRule")
        robots_rule.click()
        button = browser.find_element_by_css_selector("button[type='submit']")
        button.click()
        time.sleep(10)

    finally:
        browser.quit()


if __name__ == '__main__':
    link = "http://suninjuly.github.io/math.html"
    input_values(link)
