from selenium import webdriver
from pyperclip import copy
import math
import time
import pytest

links = ['https://stepik.org/lesson/236895/step/1',
         'https://stepik.org/lesson/236896/step/1',
         'https://stepik.org/lesson/236897/step/1',
         'https://stepik.org/lesson/236898/step/1',
         'https://stepik.org/lesson/236899/step/1',
         'https://stepik.org/lesson/236903/step/1',
         'https://stepik.org/lesson/236904/step/1',
         'https://stepik.org/lesson/236905/step/1'
         ]
words = ''


class TestStepik:


    @pytest.mark.parametrize('link', links)
    def test_stepik_feedback(self, link, browser):
        global words
        browser.get(link)
        answer = math.log(int(time.time()))
        textarea = browser.find_element_by_css_selector('textarea')
        textarea.send_keys(str(answer))
        submit_button = browser.find_element_by_css_selector('button.submit-submission')
        submit_button.click()
        optional_feedback = browser.find_element_by_css_selector('pre.smart-hints__hint')
        if optional_feedback.text != 'Correct!':
            words += optional_feedback.text
        print(optional_feedback.text)
        print(words)

# pytest -s -v --browser_name=firefox Module_3/lesson6_step3.py
