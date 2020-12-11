from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

link = "http://suninjuly.github.io/selects1.html"

def sum(x, y):
    return str(x + y)
try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element_by_css_selector("span#num1.nowrap").text)
    y = int(browser.find_element_by_css_selector("span#num2.nowrap").text)

    z = sum(x, y)
    select = Select(browser.find_element_by_class_name("custom-select"))
    select.select_by_value(z)
    browser.find_element_by_class_name("btn-default").click()
#    browser.find_element_by_css_selector("option:nth-child(2)").click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()