from .pages.main_page import MainPage
from .pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com"


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open_page()
    page.go_to_login_page()


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open_page()
    page.should_be_login_link()


def test_there_is_login_page(browser):
    main_page = MainPage(browser, link)
    main_page.open_page()
    main_page.go_to_login_page()

    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
