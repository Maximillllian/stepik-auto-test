from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# На современных страницах часто элемент моугт появляться с задержкой и мы не знаем, какая задержка стоит. Чтобы обойти
# эту проблему, можно использовать метод implicitly_wait(sec). Он будет проверять наличие нужного элекмента каждые 500мс
browser = webdriver.Chrome()

# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/wait1.html")

button = browser.find_element_by_id("verify")
button.click()
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text


# ПРИМЕР 2. Кнопка видна, но сначала неактивна. Нам надо дождаться, пока она станет активной
browser.get("http://suninjuly.github.io/wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной. Можно использовать until_not. 
button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
button.click()
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text

browser.quit()