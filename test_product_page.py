import pytest
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.locators import RegisterUser
import time

class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        register = LoginPage(browser, link)
        register.open()
        email = str(time.time()) + "@fakemail.org"
        register.register_new_user(email, "qwe123vbn")
        register_button = browser.find_element(*RegisterUser.REGISTER_BUTTON)
        register_button.click()
        register.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_to_basket_page()
        page.should_not_be_success_message()
        page.add_to_basket_page()
        page.solve_quiz_and_get_code()
        page.equal_names()
        page.equal_prices()

class TestGuestAddToBasketFromProductPage():

    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_to_basket_page()
        page.should_not_be_success_message()
        page.add_to_basket_page()
        page.solve_quiz_and_get_code()
        page.equal_names()
        page.equal_prices()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket_page()
        basket = BasketPage(browser, link)
        basket.should_not_be_basket_items()
        basket.should_basket_is_empty()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page(browser)