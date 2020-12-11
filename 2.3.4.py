from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/alert_accept.html')

try:
    browser.find_element_by_css_selector("button.btn.btn-primary").click()
    time.sleep(2)
    browser.switch_to.alert.accept()
#    time.sleep(2)
    x = browser.find_element_by_css_selector("span#input_value.nowrap").text
    y = str(math.log(abs(12*math.sin(int(x)))))
    browser.find_element_by_css_selector("input#answer.form-control").send_keys(y)
    browser.find_element_by_css_selector("button.btn.btn-primary").click()

finally:
    time.sleep(15)
    browser.quit()


