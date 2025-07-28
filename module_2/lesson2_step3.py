from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 

link = "https://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)  

    num1_element = browser.find_element(By.CSS_SELECTOR, "[id='num1']")
    num1 = num1_element.text
    num2_element = browser.find_element(By.CSS_SELECTOR, "[id='num2']")
    num2 = num2_element.text
    sum1 = int(num1) + int(num2)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(sum1)) 

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()



