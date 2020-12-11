from selenium import webdriver
import time

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
assert True

    # успеваем скопировать код за 30 секунд
time.sleep(5)
    # закрываем браузер после всех манипуляций
browser.quit()