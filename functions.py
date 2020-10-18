from pyperclip import copy
import math


def calculate_equation(x):
    res = math.log(abs(12 * math.sin(x)))
    return res


def find_x(browser):
    x = browser.find_element_by_id('input_value')
    return int(x.text)


def get_alert_answer(browser):
    answer_alert = browser.switch_to.alert
    answer = answer_alert.text.split()[-1]
    copy(answer)


def paste_answer_and_submit(browser, answer_x):
    answer_field = browser.find_element_by_id("answer")
    answer_field.send_keys(str(answer_x))
    submit_button = browser.find_element_by_css_selector("button[type='submit']")
    submit_button.click()


def calculate_selenium_math(browser):
    x = find_x(browser)
    answer = calculate_equation(x)
    paste_answer_and_submit(browser, str(answer))