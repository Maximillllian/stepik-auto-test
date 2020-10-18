import math
from selenium import webdriver
from lesson6_step4 import fill_form
import time

link = "http://suninjuly.github.io/find_link_text"
code = str(math.ceil(math.pow(math.pi, math.e)*10000))

browser = webdriver.Chrome()
browser.get(link)
link_button = browser.find_element_by_link_text(code)
link_button.click()
fill_form(browser)


