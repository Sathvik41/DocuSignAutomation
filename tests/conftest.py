from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.ie.service import Service as IEService
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture(scope='class')
def test_setup(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "ie":
        driver = webdriver.Ie(service=IEService(IEDriverManager().install()))
    elif browser == "edge":
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    driver.implicitly_wait(2)
    driver.maximize_window()
    driver.delete_all_cookies()
    request.cls.driver = driver
    yield
    # driver.quit()
