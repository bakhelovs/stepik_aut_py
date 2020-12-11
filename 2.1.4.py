from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/math.html"

# в переменную task_link вставить адрес страницы с заданием
task_link = 'https://stepik.org/lesson/165493/step/5?unit=140087'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Считать значение для переменной x. Посчитать математическую функцию от x, ввести ответ в текстовое поле
    #x = browser.find_element_by_css_selector('[id = "input_value"]').text
    #browser.find_element_by_css_selector('[id = "answer"]').send_keys(str(log(abs(12 * sin(int(x))))))

    x_element = browser.find_element_by_css_selector("span#input_value.nowrap")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option1.click()
    option1 = browser.find_element_by_css_selector("[for='robotsRule']")
    option1.click()
    button = browser.find_element_by_css_selector("button.btn.btn-default")
    button.click()

    # Отметить checkbox "Подтверждаю, что являюсь роботом". Выбрать radiobutton "Роботы рулят!". Нажать на кнопку Отправить
    #for selector in ['[for="robotCheckbox"]', '[for="robotsRule"]', '.btn']:
    #    browser.find_element_by_css_selector(selector).click()

    # Копирование числа из алерта
    alert = browser.switch_to.alert
    alert_text = alert.text
    alert.accept()
    answer = alert_text.split(': ')[-1]


finally:
    # Отправка решения на степик
    sendToStepik(task_link, answer)
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()