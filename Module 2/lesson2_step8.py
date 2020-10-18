from selenium import webdriver
import os
import time

link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)

try:
    first_name = browser.find_element_by_name("firstname")
    first_name.send_keys("Max")

    last_name = browser.find_element_by_name("lastname")
    last_name.send_keys("Raven")

    email = browser.find_element_by_name("email")
    email.send_keys("raven@mail.com")

    file_field = browser.find_element_by_id("file")
    current_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_path, "for_step8.txt")
    file_field.send_keys(file_path)

    button = browser.find_element_by_tag_name("button")
    button.click()
    time.sleep(5)
finally:
    browser.quit()