from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
#browser.implicitly_wait(12)

button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID,"price"),"$100"))
browser.find_element_by_css_selector("button#book.btn.btn-primary").click()
browser.execute_script("window.scrollBy(0, 100);")
x = browser.find_element_by_id("input_value").text
y = str(math.log(abs(12*math.sin(int(x)))))
browser.find_element_by_id("answer").send_keys(y)
browser.find_element_by_id("solve").click()

browser.quit()


