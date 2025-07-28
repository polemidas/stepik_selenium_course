from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/execute_script.html"
  
try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    input1.send_keys(y)
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    checkbox1 = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    checkbox1.click()
    radiobutton1 = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
    radiobutton1.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()

