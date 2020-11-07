from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM)

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*BasePageLocators.EMAIL)
        email_input.send_keys(email)
        password1 = self.browser.find_element(*BasePageLocators.PASSWORD1)
        password1.send_keys(password)
        password2 = self.browser.find_element(*BasePageLocators.PASSWORD2)
        password2.send_keys(password)
