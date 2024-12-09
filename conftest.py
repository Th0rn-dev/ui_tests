import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: default value - en")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options_param = "--lang="
    chrome_options = Options()
    browser = None
    if language == "en":
        print("\nstart chrome browser with language en test..")
        chrome_options.add_argument(options_param + language)
        browser = webdriver.Chrome(chrome_options)
    elif language == "fr":
        print("\nstart chrome browser with language fr test..")
        chrome_options.add_argument(options_param + language)
        browser = webdriver.Chrome(chrome_options)
    elif language == "es":
        print("\nstart chrome browser with language es test..")
        chrome_options.add_argument(options_param + language)
        browser = webdriver.Chrome(chrome_options)
    else:
        raise pytest.UsageError("--language  not input when test run!")



    yield browser
    print("\nquit browser..")
    browser.quit()