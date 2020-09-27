from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        print('should_be_login_url')
        assert self.browser.current_url == LoginPageLocators.LOGIN_URL

    def should_be_login_form(self):
        print('should_be_login_form')
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_ID), "LOGIN_FORM is not presented"

    def should_be_register_form(self):
        print('should_be_register_form')
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM_ID), "REGISTRATION_FORM is not presented"
