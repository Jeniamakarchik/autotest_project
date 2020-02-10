import pytest

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage


@pytest.mark.login_guest
@pytest.mark.parametrize('link', ['http://selenium1py.pythonanywhere.com'])
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser, link):
        page = MainPage(browser, link)
        page.open_page()
        page.go_to_login_page()

    def test_guest_should_see_login_link(self, browser, link):
        page = MainPage(browser, link)
        page.open_page()
        page.should_be_login_link()


def test_there_is_login_page(browser, link):
    main_page = MainPage(browser, link)
    main_page.open_page()
    main_page.go_to_login_page()

    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.parametrize('link', ['http://selenium1py.pythonanywhere.com'])
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser, link):
    main_page = MainPage(browser, link)
    main_page.open_page()
    main_page.should_be_basket_button()
    main_page.go_to_basket_page()

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_empty_text()


@pytest.mark.parametrize('link', ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'])
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, link):
    prod_page = ProductPage(browser, link)
    prod_page.open_page()
    prod_page.should_be_basket_button()
    prod_page.go_to_basket_page()

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_empty_text()
