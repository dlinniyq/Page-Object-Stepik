from conftest import browser
from .base_page import BasePage
from .locators import LoginPageLocators, RegisterUser

class LoginPage(BasePage):
    def should_be_login_page(self, browser):
        self.should_be_login_url(browser)
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self, browser):
        # реализуйте проверку на корректный url адрес
        assert self.is_element_present(*LoginPageLocators.LOGIN_URL), "Login url is not presented"
        assert "login" in browser.current_url

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        self.input_value(*RegisterUser.EMAIL_REGISTER, email)
        self.input_value(*RegisterUser.PASSWORD_REGISTER, password)
        self.input_value(*RegisterUser.CONFIRM_PASSWORD_REGISTER, password)