from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"
 
try:
    browser = webdriver.Chrome()
    browser.get(link) 

    button = browser.find_element(By.CSS_SELECTOR, "button.trollface")
    button.click()

    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)

    x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    input1.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
