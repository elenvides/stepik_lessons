from selenium import webdriver
from sys import argv
import time

script_name, link = argv
browser = webdriver.Chrome()

# run:
# python module_2/test_registration.py http://suninjuly.github.io/registration1.html - without errors
# python module_2/test_registration.py http://suninjuly.github.io/registration2.html - with error

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input_first_name = browser.find_element_by_css_selector(".first_block .first")
    input_first_name.send_keys("Ivan")
    input_last_name = browser.find_element_by_css_selector(".first_block .second")
    input_last_name.send_keys("Petrov")
    input_email = browser.find_element_by_class_name("third")
    input_email.send_keys("testmai@test.ua")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
