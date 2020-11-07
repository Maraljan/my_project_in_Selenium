from telnetlib import EC
# TODO pls remove these imports
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from conftest import browser
from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):

    def check_is_basket_empty(self):
        assert 'Ваша корзина пуста' in self.browser.find_element(*BasketPageLocators.EMPTY_BASKET).text

    def check_is_product_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_PRODUCT)

