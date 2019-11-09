import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language(for example fr")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    print("\nstart chrome browser for test..")
    # нет админских прав на комп - приходится путь к драйверу явно указывать ))
    browser = webdriver.Chrome("d://1//chromedriver.exe", options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()



