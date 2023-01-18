import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

@pytest.fixture
def setup_webdriver():
    return webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

def test_go_to_google(setup_webdriver):
    driver = setup_webdriver
    driver.get("http://www.google.com")
    time.sleep(3)

def test_go_to_aftonbladet(setup_webdriver):
    driver = setup_webdriver
    driver.get("http://www.aftonbladet.se")
    time.sleep(3)
