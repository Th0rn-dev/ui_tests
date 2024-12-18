from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    DONT_PRESENT = "Button add product not present on page"
    DONT_ADDED_TO_BASKET = "Product dont added to basket"

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD), \
            self.DONT_PRESENT

    def product_params(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text,
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return product_name[0], product_price

    def should_add_product_to_basket(self, product_name, product_price):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD)
        button.click()
        self.solve_quiz_and_get_code()
        product_name_in_alert = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_IN_ALERT)
        assert product_name == product_name_in_alert.text, self.DONT_ADDED_TO_BASKET
        total = self.browser.find_element(*ProductPageLocators.ALERT_INFO)
        assert product_price in total.text, self.DONT_ADDED_TO_BASKET

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
