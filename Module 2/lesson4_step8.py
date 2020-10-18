from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from functions import *
import time

link = "http://suninjuly.github.io/explicit_wait2.html"

browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get(link)

try:
    WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    book = browser.find_element_by_id("book")
    book.click()

    calculate_selenium_math(browser)

    time.sleep(3)

    get_alert_answer(browser)
finally:
    browser.quit()
