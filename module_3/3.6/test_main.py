import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import math
import time
from dotenv import load_dotenv
import os

# Загружаем переменные окружения из .env
load_dotenv()
EMAIL = os.getenv("STEPIC_EMAIL")
PASSWORD = os.getenv("STEPIC_PASSWORD")

@pytest.mark.parametrize('number', [
    "236895", "236896", "236897", "236898",
    "236899", "236903", "236904", "236905"
])
def test_hardmode(browser, number):
    # Формируем ссылку на урок
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser.get(link)

    # Кнопка "Войти"
    button1 = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.navbar__auth_login"))
    )
    button1.click()

    # Ввод email и пароль из .env
    input1 = browser.find_element(By.CSS_SELECTOR, "#id_login_email")
    input1.send_keys(EMAIL)

    input2 = browser.find_element(By.CSS_SELECTOR, "#id_login_password")
    input2.send_keys(PASSWORD)

    # Кнопка "Войти"
    button2 = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.sign-form__btn"))
    )
    button2.click()

    # Проверка кнопки "Решить снова"
    try:
        button3 = WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.again-btn"))
        )
        button3.click()
        print('Кнопка "Решить снова" обнаружена, поле textarea неактивное')
    except TimeoutException:
        print('Кнопка "Решить снова" не обнаружена, поле textarea активное')

    finally:
        # Ждем, пока textarea станет активной
        WebDriverWait(browser, 10).until_not(
            EC.element_attribute_to_include((By.CSS_SELECTOR, "textarea.ember-text-area"), 'disabled')
        )

        # Вводим ответ
        answer = math.log(int(time.time()))
        input3 = WebDriverWait(browser, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "textarea.ember-text-area"))
        )
        input3.send_keys(answer)

        # Кнопка "Отправить"
        button4 = WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
        )
        button4.click()

        # Проверка фидбека
        feedback = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "p.smart-hints__hint"))
        )
        assert feedback.text == "Correct!", f"{feedback.text}"
