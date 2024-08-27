import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: en or ru")

@pytest.fixture()
def browser(request):
    language = request.config.getoption("language")
    if language == "en":
        browser_language = "en"
    elif language == "ru":
        browser_language = "ru"
    else:
        raise pytest.UsageError("--language should be en or ru")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
    browser = webdriver.Chrome(options=options)

    yield browser
    print("\nquit browser..")
    browser.quit()
