from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import utilities.custom_logger as cl
import logging


class CustomDriver():
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == 'id':
            return By.ID
        elif locatorType == 'name':
            return By.NAME
        elif locatorType == 'xpath':
            return By.XPATH
        elif locatorType == 'css':
            return By.CSS_SELECTOR
        elif locatorType == 'classname':
            return By.CLASS_NAME
        elif locatorType == 'linktext':
            return By.LINK_TEXT
        else:
            self.log.info(f'Locator type {locatorType} is not correct/supported')
            return False

    def get_element(self, locator, locatorType='css'):
        element = None
        try:
            locatorType == locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info(f'Element Found with locator {locator} and locatorType {locatorType}')
        except:
            self.log.info(f'Element not Found with locator {locator} and locatorType {locatorType}')
        return element

    def get_value_css(self, locator, locatorType='css', param='color'):
        element_value_css = None
        try:
            element = self.get_element(locator, locatorType)
            element_value_css = element.value_of_css_property(param)
            self.log.info(f'Element value CSS {param} Found with locator {locator} and locatorType {locatorType}')
        except:
            self.log.info(f'Element value CSS {param} not Found with locator {locator} and locatorType {locatorType}')
        return element_value_css

    def element_click(self, locator, locatorType='id'):
        try:
            element = self.get_element(locator, locatorType)
            element.click()
            self.log.info('Clicked on the element with locator: ' + locator + 'locatorType: ' + locatorType)
        except:
            self.log.info('Cannot click on the element with locator' + locator + 'locatorType: ' + locatorType)
            print_stack()

    def element_hover(self, locator, locatorType='css'):
        try:
            element = self.get_element(locator, locatorType)
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            self.log.info(f'Hovered on the element with locator: {locator}  locatorType:  {locatorType}')
        except:
            self.log.info(f'Cannot hover on the element with locator {locator} locatorType: {locatorType}')
            print_stack()



