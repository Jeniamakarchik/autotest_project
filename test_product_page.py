import pytest

from .pages.product_page import ProductPage


# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#                                                "?promo=offer7", marks=pytest.mark.xfail),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# def test_adding_to_the_basket(browser, link):
#     prod_page = ProductPage(browser, link)
#     prod_page.open_page()
#     prod_page.should_be_add_to_cart_btn()
#     prod_page.add_to_cart()
#     prod_page.solve_quiz_and_get_code()
#     prod_page.should_be_item_in_cart()

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    prod_page = ProductPage(browser, link)
    prod_page.open_page()
    prod_page.should_be_add_to_cart_btn()
    prod_page.add_to_cart()
    prod_page.should_not_be_success_message()


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_guest_cant_see_success_message(browser, link):
    prod_page = ProductPage(browser, link)
    prod_page.open_page()
    prod_page.should_not_be_success_message()


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    prod_page = ProductPage(browser, link)
    prod_page.open_page()
    prod_page.should_be_add_to_cart_btn()
    prod_page.add_to_cart()
    prod_page.should_disappear()
