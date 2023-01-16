import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help="Choose language: ru or en")

@pytest.fixture(scope="function")
def browser(request):
    options = Options()
    user_language = request.config.getoption('language')
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    print("\nstart browser for test..")
    browser = webdriver.Chrome('chromedriver', options=options)

    yield browser
    print("\nquit browser..")
    #input()
    browser.quit()