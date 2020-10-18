# alert - окно браузера, которое необходимо закрыть перед тем, как работать дальше. В этом курсе в этом окне были
# ответы

from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.execute_script("alert('Hide me!');")
time.sleep(3)

alert = browser.switch_to.alert

# Распечатываем текст в alert
alert_text = alert.text
print(alert_text)

# Нажимаем ok
alert.accept()

# В окнах где две кнопки: Отмена и ок, помимо accept(), можно отменить с помощью dismiss(). Если есть поле для ввода
# то туда ввести значение можно с помощью send_keys()

time.sleep(3)

# Можно переключаться между вкладками браузера. Для этого нужно знать имя новой вкладки браузера
new_window = browser.window_handles[1]

# И лучше запомнить изначальную вкладку
first_window = browser.window_handles[0]

# Переключение проиходит так
browser.switch_to.window(new_window)

browser.quit()