import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.fixture()
def driver():
    _ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    _DRIVER_PATH = _ROOT_DIR + '/chromedriver'
    os.environ["webdriver.chrome.driver"] = _DRIVER_PATH
    caps = DesiredCapabilities().CHROME
    driver = webdriver.Remote('http://localhost:4444/wd/hub', desired_capabilities=caps)
    driver.implicitly_wait(15)
    driver.set_window_position(1930, 0)
    driver.maximize_window()
    return driver
