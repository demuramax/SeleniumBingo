import time
from selenium.webdriver.common.by import By
import pytest
import utilities.custom_logger as cl
import logging
from base.CustomDriver import CustomDriver


class BingoPage(CustomDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    BINGO_VARIANTS = "col-md-12"


    def test_bingo(self):
        element = self.get_element(self.BINGO_VARIANTS, locatorType='classname')
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(2)
