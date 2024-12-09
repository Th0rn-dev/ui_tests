from pages.base_page import BasePage
from pages.locators import AddToBasketLocator


class ProductPage(BasePage):

    DONT_PRESENT = "Button add product not present on page"
    DONT_ADDED_TO_BASKET = "Product dont added to basket"

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*AddToBasketLocator.BUTTON_ADD), \
            self.DONT_PRESENT

    def product_params(self):
        product_name = self.browser.find_element(*AddToBasketLocator.PRODUCT_NAME).text,
        product_price = self.browser.find_element(*AddToBasketLocator.PRODUCT_PRICE).text
        return product_name[0], product_price


    def should_add_product_to_basket(self, product_name, product_price):
        button = self.browser.find_element(*AddToBasketLocator.BUTTON_ADD)
        button.click()
        self.solve_quiz_and_get_code()
        successes = self.browser.find_elements(*AddToBasketLocator.SUCCESSES)
        assert (product_name in successes[0].text), (
            self.DONT_ADDED_TO_BASKET)
        total = self.browser.find_element(*AddToBasketLocator.ALERT_INFO)
        assert product_price in total.text, self.DONT_ADDED_TO_BASKET
