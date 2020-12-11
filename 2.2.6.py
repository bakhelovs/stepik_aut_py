from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    x = browser.find_element_by_css_selector("span#input_value.nowrap").text
    y = calc(x)
    browser.find_element_by_css_selector("input#answer.form-control").send_keys(y)
    browser.execute_script("window.scrollBy(0, 100);")
    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()
    browser.find_element_by_css_selector("button.btn.btn-primary").click()

finally:

    time.sleep(10)
    browser.quit()
