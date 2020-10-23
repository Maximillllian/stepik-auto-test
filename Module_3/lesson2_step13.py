import unittest
import time
from selenium import webdriver


def fill_form(browser):
    required_field_one = browser.find_element_by_css_selector(".first_block input[class = 'form-control first']")
    required_field_one.send_keys("Fuck yeah!")
    required_field_two = browser.find_element_by_css_selector(".first_block input[class = 'form-control second']")
    required_field_two.send_keys("Fuck yeah!")
    required_field_three = browser.find_element_by_css_selector(".first_block input[class = 'form-control third']")
    required_field_three.send_keys("Fuck yeah!")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций


class TestsModuleOne(unittest.TestCase):
    browser = webdriver.Chrome()

    def test_one(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.browser.get(link)
        fill_form(self.browser)

    def test_two(self):
        link = "http://suninjuly.github.io/registration2.html"
        self.browser.get(link)
        fill_form(self.browser)


if __name__ == '__main__':
    unittest.main()