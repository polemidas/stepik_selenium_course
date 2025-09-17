import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    """
    Фикстура для запуска и закрытия браузера Chrome.
    Доступна для всех тестов в текущей папке и дочерних.
    """
    print("\nStart browser for test..")
    options = webdriver.ChromeOptions()
    # отключаем лишние сообщения в консоли Chrome
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    yield driver
    print("\nQuit browser..")
    driver.quit()