# Тесты можно маркировать по каким-нибудь категориям. Например модно обозначить тест как smoke - критичный, то есть
# его надо запускать на каждый коммит разработчиков. А можно пометить как, например, regression  - он должен запускаться
# перед релизом. Перед тестом нужно вставить следующий декоратор @pytest.mark.название

import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1:

    # маркируем тест
    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    @pytest.mark.win10
    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")


# Тесты с определенной марикровкой запускаются из консоли добавлением "-m (название теста)"
# pytest -s -m smoke PyTest_marks.py

# На всякий случай можно занести все метки в отдельный файл pytest.ini. Смотри в корне проекта

# Чтобы запустить все тесты кроме помеченнных меткой, после -m нужно добавить "not smoke", для запуска тестов двух и
# более меток используется "smoke or regression", для тестов, коотрые помечены двумя метками и только ими, используется
# "win10 and regression"

# Чтобы пропустить тест во время запуска всех тестов, используется @pytest.mark.skip

# Можно пометить тест как ожидаемо падающий. Когда мы знаем про баг, но его еще не починили. Тогда нужно использовать
# @pytest.mark.xfail. Если такой тест неожидано успешно проходит проверку, в консоли будет выведено XPASS. Тогда мы
# поймем, что баг исправили. 
