# Запускать тесты можно с помощью пакета PyTest. В консоли нужно прописать "pytest (название файла/директории)"
# Тесты должны быть расположены в функциях с названием начинающимся/заканчивающимся на test

# Фикстуры делают что-то до или после одного теста. Если функция фикстуры начинается на setup, она выполняется до теста
# Если с teardown - после теста. Например - открытие и закрытие браузера

from selenium import webdriver
import pytest

link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage1:

    def setup_method(self):
        print("\nstart browser for test..")
        self.browser = webdriver.Chrome()

    def teardown_method(self):
        print("quit browser for test..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")


# Фикстуры могут возвращать значение. Для этого функцию-фикстуру надо обернуть декоратором @pytest.fixture. Чтобы после
# завершения теста выполнился еще какой-то код, нужно вместо return ставить yield
@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()


class TestMainPage2:
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")

# Для фикстур можно задавать область покрытия фикстур. Допустимые значения: “function”, “class”, “module”, “session”.
# Соответственно, фикстура будет вызываться один раз для тестового метода, один раз для класса, один раз для модуля
# или один раз для всех тестов, запущенных в данной сессии
@pytest.fixture(scope="class")
def browser():
    return

# Если в скобках указать utouse=True, то фикстура будет запускаться для каждого теста