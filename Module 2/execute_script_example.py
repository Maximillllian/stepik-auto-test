from selenium import webdriver
import time

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"

# Кнопку закрывает нижняя часть сайт сайта, поэтому мы не сможем кликнуть на нее
try:
    browser.get(link)
    button = browser.find_element_by_tag_name("button")
    time.sleep(3)

    # Мы прокручиваем страницу до момента, пока кнопка не будет видна
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    time.sleep(3)
    button.click()
finally:
    browser.quit()

# Можно заскролить на конкретное число пикселей browser.execute_script("window.scrollBy(0, 100);")
