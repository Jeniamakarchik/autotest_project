from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)

    def should_be_add_to_cart_btn(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON)

    def add_to_cart(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def should_be_equal_names(self):
        items_strong = self.browser.find_elements(*ProductPageLocators.BASKET_STRONG_NAMES)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        names_equal = False
        for item in items_strong:
            if item.text == product_name:
                names_equal = True
        assert names_equal, "Names of product isn't equal"

    def should_be_equal_cost(self):
        item_basket_cost = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL)
        item_product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        assert item_basket_cost.text == item_product_cost.text, "Prices in basket and in product page isn't equal"

    def should_be_item_in_cart(self):
        self.should_be_equal_names()
        self.should_be_equal_cost()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message should disappear, but not"
