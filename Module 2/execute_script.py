from selenium import webdriver
import time

browser = webdriver.Chrome()

# Иногда встроенных инструментов Selenium не хватает, поэтому есть метод execute_script. В него забивают JavaScript
# код.
browser.execute_script("document.title='Script executing';")
browser.execute_script("alert('Robots at work');")

# Скрипты можно перечислять через точку с запятой
browser.execute_script("document.title='Script executing';alert('Robots at work');")

browser.quit()