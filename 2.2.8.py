from selenium import webdriver
import os
import time

    #запускать через cmd из того же каталога где лежит прикрепляемый файл

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    browser.find_element_by_name("firstname").send_keys("AA")
    browser.find_element_by_name("lastname").send_keys("BB")
    browser.find_element_by_name("email").send_keys("CC@CC.COM")
    #    fills = browser.find_elements_by_css_selector("input[required]")
    #    for element in fills:
    #        element.send_keys("ABC")

    # получаем путь к директории текущего исполняемого скрипта lesson2_7.py
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # получаем путь к file_example.txt
    file_path = os.path.join(current_dir, "new1.txt")
    # отправляем файл
    browser.find_element_by_css_selector("input#file").send_keys(file_path)
    browser.find_element_by_css_selector("button.btn.btn-primary").click()
finally:

    time.sleep(5)
    browser.quit()

#    print(current_dir)
#    print(file_path)
