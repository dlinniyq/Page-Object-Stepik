from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET = (By.CSS_SELECTOR, "span>a.btn.btn-default")

class  LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class RegisterUser():
    EMAIL_REGISTER = (By.CSS_SELECTOR, "[name = 'registration-email']")
    PASSWORD_REGISTER = (By.CSS_SELECTOR, "[name = 'registration-password1']")
    CONFIRM_PASSWORD_REGISTER = (By.CSS_SELECTOR, "[name = 'registration-password2']")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name = 'registration_submit']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_URL = (By.CSS_SELECTOR, "#add_to_basket_form>button")
    CHOOSE_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main>h1")
    ADDED_NAME = (By.CSS_SELECTOR, "#messages>div:nth-child(1) strong")
    CHOOSE_PRICE = (By.CSS_SELECTOR, "p.price_color")
    ADDED_PRICE = (By.CSS_SELECTOR, "#messages>div:nth-child(3) strong")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner>p")

class ProductPageLocators():
    ADDED_TO_BASKET_NOTIFICATION = (By.CSS_SELECTOR, "#messages>div:nth-child(1)")