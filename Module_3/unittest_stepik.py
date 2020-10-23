# Для проведения сразу нескольких тестов лучше использоватьь сторонние библиотеки, например unittest, PyTest или nose
# Сейчас рассмотрим unittest - строенную и не самую лучшую

import unittest

# В unittest все тесты должны быть в отдельном классе, который наследуется от TestCase


class TestAbs(unittest.TestCase):

    # Тесты должны начинаться с test_
    def test_abs1(self):
        self.assertEqual(abs(-42), 42, "Should be absolute value of number")

    def test_abs2(self):
        self.assertEqual(abs(-42), -42, "Should be absolute value of number")


if __name__ == "__main__":
    unittest.main()