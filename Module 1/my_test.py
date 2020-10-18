from selenium import webdriver
import time

link = "https://docs.google.com/forms/d/e/1FAIpQLSdsw1lfti1Lc2F4CGylBRtlybU7rZfXptCy4CpdCrrlCRKrPw/viewform"

try:
    browser = webdriver.Chrome()
    for j in range(100):
        browser.get(link)
        time.sleep(1)
        fields = browser.find_elements_by_css_selector("input[type = 'text']")
        print(fields)
        for i in fields:
            i.send_keys("Никита Пидор")
        span = browser.find_element_by_xpath("//span[text() = 'Не Макс']")
        span.click()
        time.sleep(1)
        button = browser.find_element_by_xpath("//span[text() = 'Отправить']")
        button.click()
finally:
    browser.quit()