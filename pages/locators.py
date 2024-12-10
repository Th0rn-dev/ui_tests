from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.ID, "#ligin_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators():
    LOGIN_URL = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"
    LOGIN_FROM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    SUCCESS_MESSAGE = (By.CLASS_NAME, "any")
    BUTTON_ADD = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME_IN_ALERT = (By.CSS_SELECTOR,
                             "#messages > div:nth-child(1) > div > strong")
    ALERT_INFO = (By.CLASS_NAME, "alert-info")
    PRODUCT_NAME = (By.CSS_SELECTOR,
                    '#content_inner > article > div.row > div.col-sm-6.product_main > h1')
    PRODUCT_PRICE = (By.CLASS_NAME, "price_color")

