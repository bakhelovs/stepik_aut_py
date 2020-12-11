from selenium import webdriver
import unittest
import time

class PythonRegistration1(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_fill_form(self):
        browser = self.browser
        browser.get("http://suninjuly.github.io/registration1.html")

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector(".first_block .first")
        input1.send_keys("Vasya")
        input2 = browser.find_element_by_css_selector(".first_block .second")
        input2.send_keys("Pupkin")
        input3 = browser.find_element_by_css_selector(".first_block .third")
        input3.send_keys("a@a.ru")
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        welcome_text_check = "Congratulations! You have successfully registered!"
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text_check, welcome_text)

    def test_fill_form2(self):
        browser = self.browser
        browser.get("http://suninjuly.github.io/registration2.html")

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector(".first_block .first")
        input1.send_keys("Vasya")
        input2 = browser.find_element_by_css_selector(".first_block .second")
        input2.send_keys("Pupkin")
        input3 = browser.find_element_by_css_selector(".first_block .third")
        input3.send_keys("a@a.ru")
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        welcome_text_check = "Congratulations! You have successfully registered!"
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text_check, welcome_text)




    def tearDown(self):
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        #time.sleep(10)
        # закрываем браузер после всех манипуляций
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()