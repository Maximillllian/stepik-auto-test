from selenium import webdriver
from functions import calculate_equation, find_x, get_alert_answer, paste_answer_and_submit

link = "http://suninjuly.github.io/redirect_accept.html"

browser = webdriver.Chrome()
browser.get(link)

try:
    redirect_button = browser.find_element_by_tag_name("button")
    redirect_button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = find_x(browser)
    answer_x = calculate_equation(x)

    paste_answer_and_submit(browser, answer_x)

    get_alert_answer(browser)

finally:
    browser.quit()