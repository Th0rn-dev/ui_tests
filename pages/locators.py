from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#ligin_link")


class LoginPageLocators():
    LOGIN_URL = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"
    LOGIN_FROM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class AddToBasketLocator():
    BUTTON_ADD = (By.CLASS_NAME, "btn-add-to-basket")
    SUCCESSES = (By.CLASS_NAME, "alert-success")
    ALLERT_INFO = (By.CLASS_NAME, "alert-info")
