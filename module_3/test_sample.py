"""
Тестовый сценарий 2.2.1 Переход в карточку товара по названию
Предусловия:
1. Иметь книгу в каталоге, книга должна быть в наличии
2. Открыть главную страницу
3. Перейти в каталог -> все товары
Шаги:
- 1. В блоке первого товара нажать на название
-- Переадрессация в карточку товара
-- Название товара совпадает с названием из каталога
"""

from selenium import webdriver

main_page_link = "http://selenium1py.pythonanywhere.com/ru/"

catalogue_all_products_locator = 'a[href="/ru/catalogue/"]'
catalog_product_card_locator = 'article.product_pod'
catalog_product_title_locator = 'h3 a'
product_page_title_locator = 'h1'


def test_open_product_by_title():

    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(main_page_link)

        catalog_all = browser.find_element_by_css_selector(catalogue_all_products_locator)
        catalog_all.click()

        # Act
        catalog_first_product_card = browser.find_element_by_css_selector(catalog_product_card_locator)

        first_product_title = catalog_first_product_card.find_element_by_css_selector(catalog_product_title_locator)
        catalog_product_title_text = first_product_title.text
        first_product_title.click()

        product_page_title = browser.find_element_by_css_selector(product_page_title_locator)

        # Assert
        product_page_title_text = product_page_title.text
        assert product_page_title_text == catalog_product_title_text, \
            f"Product page title is '{catalog_product_title_text}', " \
            f"but expected (title in catalog) is '{catalog_product_title_text}'"

    finally:
        browser.quit()


test_open_product_by_title()
