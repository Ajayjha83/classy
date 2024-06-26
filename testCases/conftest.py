import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from webdriver_manager.safari import SafariDriverManager
from webdriver_manager.opera import OperaDriverManager
# from webdriver_manager.iedriver import IEDriverManager


@pytest.fixture()
def setup():
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    driver = webdriver.Chrome()

    yield driver

    driver.quit()
