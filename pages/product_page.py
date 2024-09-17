from pages.base_page import BasePage
from .locators import BasketPageLocators, ProductPageLocators

class ProductPage(BasePage):

    def add_to_basket_page(self):
        basket_link = self.browser.find_element(*BasketPageLocators.BASKET_URL)
        basket_link.click()

    def should_be_add_to_basket_page(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_URL), "Basket page is not presented"

    def equal_names(self):
        self.is_text_equal(*BasketPageLocators.ADDED_NAME, *BasketPageLocators.CHOOSE_NAME)

    def equal_prices(self):
        self.is_text_equal(*BasketPageLocators.CHOOSE_PRICE, *BasketPageLocators.ADDED_PRICE)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDED_TO_BASKET_NOTIFICATION),\
            "Added to basket message is presented, but should not be"