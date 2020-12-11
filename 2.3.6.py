from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")

try:
    browser.find_element_by_css_selector("button.trollface.btn.btn-primary").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = browser.find_element_by_css_selector("span#input_value.nowrap").text
    y = str(math.log(abs(12*math.sin(int(x)))))
    browser.find_element_by_css_selector("input#answer.form-control").send_keys(y)
    browser.find_element_by_css_selector("button.btn.btn-primary").click()

finally:

    time.sleep(5)
    browser.quit()


