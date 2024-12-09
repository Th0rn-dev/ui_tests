import time

from pages.product_page import ProductPage


def test_should_add_product_in_basket(browser):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_add_to_basket_button()
    product_name, product_price = product_page.product_params()
    product_page.should_add_product_to_basket(product_name, product_price)
