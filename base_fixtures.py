import pytest
from config.config1 import *
from selenium import webdriver


class DriverInit:

    @pytest.fixture(scope='class', autouse=True)
    def driver_init(self, request):
        if browser.lower() == "chrome":
            driver = webdriver.Chrome(executable_path=chrome_path)
        elif browser.lower() == 'firefox':
            driver.webdriver.Firefox()
        request.cls.driver = driver
        driver.get(URL)
        driver.maximize_window()
        yield
        driver.close()
