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

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),\
            "Success message is presented, but should not be"

    def should_be_disappeared_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message should be disappeared"

