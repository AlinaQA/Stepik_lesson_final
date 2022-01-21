import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    if language == False:
        raise pytest.UsageError("--language unknown")
    options = Options()
    # options.add_experimental_option('prefs', {'intl.accept_languages': language})
    options.add_argument("--lang=en")
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()