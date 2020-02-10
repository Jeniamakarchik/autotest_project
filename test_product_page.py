import time

import pytest

from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
                                               "?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_adding_to_the_basket(browser, link):
    prod_page = ProductPage(browser, link)
    prod_page.open_page()
    prod_page.should_be_add_to_cart_btn()
    prod_page.add_to_cart()
    prod_page.solve_quiz_and_get_code()
    prod_page.should_be_item_in_cart()


@pytest.mark.basket_user
@pytest.mark.parametrize('link', ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'])
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        page = LoginPage(browser, url=link)
        page.open_page()

        email = str(time.time()) + '@fakemail.org'
        password = 'helloworld1'

        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser, link):
        prod_page = ProductPage(browser, link)
        prod_page.open_page()
        prod_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, link):
        prod_page = ProductPage(browser, link)
        prod_page.open_page()
        prod_page.should_be_add_to_cart_btn()
        prod_page.add_to_cart()


@pytest.mark.basket_guest
@pytest.mark.parametrize('link', ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'])
class TestGuestAddToBasketFromProductPage:
    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser, link):
        prod_page = ProductPage(browser, link)
        prod_page.open_page()
        prod_page.should_be_add_to_cart_btn()
        prod_page.add_to_cart()
        prod_page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser, link):
        prod_page = ProductPage(browser, link)
        prod_page.open_page()
        prod_page.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser, link):
        prod_page = ProductPage(browser, link)
        prod_page.open_page()
        prod_page.should_be_add_to_cart_btn()
        prod_page.add_to_cart()
        prod_page.should_disappear()

    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser, link):
        prod_page = ProductPage(browser, link)
        prod_page.open_page()
        prod_page.should_be_add_to_cart_btn()
        prod_page.add_to_cart()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser, link):
        prod_page = ProductPage(browser, link)
        prod_page.open_page()
        prod_page.should_be_basket_button()
        prod_page.go_to_basket_page()

        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_empty_basket()
        basket_page.should_be_empty_text()


@pytest.mark.login_prod_guest
@pytest.mark.parametrize('link', ['http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'])
class TestGuestGoToLoginPageFromProductPage:
    def test_guest_should_see_login_link_on_product_page(self, browser, link):
        page = ProductPage(browser, link)
        page.open_page()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser, link):
        page = ProductPage(browser, link)
        page.open_page()
        page.should_be_login_link()
        page.go_to_login_page()

        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
