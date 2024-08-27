from conftest import browser
from selenium.webdriver.common.by import By

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    browser.implicitly_wait(3)
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()