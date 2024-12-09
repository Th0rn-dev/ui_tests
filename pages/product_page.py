from pages.base_page import BasePage
from pages.locators import AddToBasketLocator


class ProductPage(BasePage):
    DONT_PRESENT = "Button add product not present on page"
    DONT_ADDED_TO_BASKET = "Product dont added to basket"

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*AddToBasketLocator.BUTTON_ADD), \
            self.DONT_PRESENT

    def should_add_product_to_basket(self):
        button = self.browser.find_element(*AddToBasketLocator.BUTTON_ADD)
        button.click()
        self.solve_quiz_and_get_code()
        successes = self.browser.find_elements(*AddToBasketLocator.SUCCESSES)
        assert ("The shellcoder's handbook" in successes[0].text), (
            self.DONT_ADDED_TO_BASKET)
        total = self.browser.find_element(*AddToBasketLocator.ALLERT_INFO)
        assert "£9.99" in total.text, self.DONT_ADDED_TO_BASKET
