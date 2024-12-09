import time
from selenium.webdriver.common.by import By


def test_button_adds_items_exists(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    basket = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    assert "Añadir al carrito" == basket.text