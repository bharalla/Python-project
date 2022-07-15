import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):

    if browser == 'chrome':
        driver = webdriver.Chrome("C:/myProject/pythonProject/drivers/chromedriver.exe")
        driver.maximize_window()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'ie':
        driver = webdriver.Ie()
    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
