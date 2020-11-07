import time

import pytest

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from test_main_page import LOGIN_URL


@pytest.mark.login
class TestLoginFromProductPage:
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.go_to_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_add_product_to_basket(self, browser):
        product = ProductPage(browser, self.link)
        product.open()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, LOGIN_URL)
    page.open()
    page.click_to_basket()
    basket_page = BasketPage(browser, page.browser.current_url)
    basket_page.open()
    basket_page.check_is_product_empty()
    basket_page.check_is_basket_empty()


class TestUserAddToBasketFromProductPage:
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = f'{str(time.time())}@fakemail.org'
        password = '123456789'
        register = LoginPage(browser, self.link)
        register.open()
        register.go_to_login_page()
        register.register_new_user(email, password)

    def test_user_cant_see_success_message(self, browser):
        product = ProductPage(browser, self.link)
        product.open()
        product.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        product = ProductPage(browser, self.link)
        product.open()
        product.add_basket()
