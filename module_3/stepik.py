from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

answer = math.log(int(time.time()))
link = "https://stepik.org/lesson/236895/step/1"

try:
    browser = webdriver.Chrome()
    browser.get(link) 

    time.sleep(2)
     
    button = browser.find_element(By.CSS_SELECTOR, "[id='ember484']")
    button.click()

    input1 = browser.find_element(By.CSS_SELECTOR, "[name='login']")
    input1.send_keys("viktarmasliakou@gmail.com")
    input2 = browser.find_element(By.CSS_SELECTOR, "[name='password']")
    input2.send_keys("Bangels161!q")

    button = browser.find_element(By.XPATH, "//*[@id='login_form']/button")
    button.click()

    time.sleep(2)

    input3 = browser.find_element(By.CSS_SELECTOR, "textarea.ember-text-area.textarea.string-quiz__textarea") 
    input3.send_keys(answer)

    button = browser.find_element(By.CSS_SELECTOR, "button.submit-submission")
    button.click()
    
    
finally:
    time.sleep(30)
    browser.quit()
