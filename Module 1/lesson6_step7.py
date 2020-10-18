from selenium import webdriver
import time

link = "http://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    fields = browser.find_elements_by_tag_name("input")
    for i in fields:
        i.send_keys("Fuck yeah!")
    button = browser.find_element_by_tag_name("button")
    button.click()
    time.sleep(30)
finally:
    browser.quit()