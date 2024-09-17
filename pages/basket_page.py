from pages.base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_basket_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS),\
            "Basket items is presented, but should not be"

    def should_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), \
            "Basket is not empty"