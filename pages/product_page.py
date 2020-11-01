from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BASKET)
        button.click()
        self.solve_quiz_and_get_code()

    def check_message(self):
        assert self.browser.find_element(*ProductPageLocators.TITLE).text == \
               self.browser.find_element(*ProductPageLocators.TITLE1).text

    def check_price(self):
        assert self.browser.find_element(*ProductPageLocators.PRICE).text == \
               self.browser.find_element(*ProductPageLocators.PRICE1).text
