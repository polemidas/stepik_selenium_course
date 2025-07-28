from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import os 

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link) 
     
    input1 = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    input1.send_keys("Thomas")
    input2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    input2.send_keys("Anderson")
    input2 = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    input2.send_keys("t.anderson@local.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file_example.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)
   
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
