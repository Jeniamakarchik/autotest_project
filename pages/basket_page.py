from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS)

    def should_be_empty_text(self):
        assert 'empty' in self.browser.find_element(*BasketPageLocators.EMPTY_MESSAGE).text, 'There is no empty text.'
