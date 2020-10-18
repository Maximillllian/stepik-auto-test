from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_id("submit_button")
    button.click()
finally:
    browser.quit()

# find_element_by_id — поиск по уникальному атрибуту id элемента. Если ваши разработчики проставляют всем элементам в
# приложении уникальный id, то вам повезло, и вы чаще всего будет использовать этот метод, т.к. он наиболее стабильный;

# find_element_by_css_selector — поиск элемента с помощью правил на основе CSS. Это универсальный метод поиска, так как
# большинство веб-приложений использует CSS для вёрстки и задания оформления страницам. Если find_element_by_id вам не
# подходит из-за отсутствия id у элементов, то скорее всего вы будете использовать именно этот метод в ваших тестах;

# find_element_by_xpath — поиск с помощью языка запросов XPath, позволяет выполнять очень гибкий поиск элементов;
# find_element_by_name — поиск по атрибуту name элемента;
# find_element_by_tag_name — поиск элемента по названию тега элемента;
# find_element_by_class_name — поиск по значению атрибута class;
# find_element_by_link_text — поиск ссылки на странице по полному совпадению;

# find_element_by_partial_link_text — поиск ссылки на странице, если текст селектора совпадает с любой частью текста
# ссылки.

# ЕСЛИ ИСПОЛЬЗОВАТЬ elements ВМЕСТО element, то найдутся все 

# Альтернативный способ

# By.ID – поиск по уникальному атрибуту id элемента;
# By.CSS_SELECTOR – поиск элементов с помощью правил на основе CSS;
# By.XPATH – поиск элементов с помощью языка запросов XPath;
# By.NAME – поиск по атрибуту name элемента;
# By.TAG_NAME – поиск по названию тега;
# By.CLASS_NAME – поиск по атрибуту class элемента;
# By.LINK_TEXT – поиск ссылки с указанным текстом. Текст ссылки должен быть точным совпадением;
# By.PARTIAL_LINK_TEXT – поиск ссылки по частичному совпадению текста.

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(5)
    button = browser.find_element(By.ID, "submit_button")
    button.click()
finally:
    browser.quit()
