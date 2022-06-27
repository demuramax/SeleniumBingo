import time
from selenium.webdriver.common.by import By
import pytest
import utilities.custom_logger as cl
import logging
from base.CustomDriver import CustomDriver


class HomePage(CustomDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    POPUP_CONFIRM = ".top-btn"
    HOME_LINK = "a[title='Home']"
    PRODUCTS_LINK = "a[title='Games']"
    CLIENT_HUB = "//a[@href='https://clienthub.pragmaticplay.com/']"
    COMPANY_LINK = "Company"
    NEWS_LINK = "News"
    CONTACT_LINK = "//a[@href='https://pragmaticplay.com/en/contact#form']"
    BINGO_LINK = "Bingo"
    PRODUCTS_BTN_ARROW = "//a[@title='Games']/div"
    COMPANY_BTN_ARROW = "//ul[@id='menu-top-menu']/li[4]//div[@class='arrow-menu']"

    def close_home_popup(self):
        self.driver.find_element(By.CSS_SELECTOR, '.top-btn').click()

    def test_home_link(self):
        home_btn_color = self.get_value_css(self.HOME_LINK)
        print('Color of button is ' + home_btn_color)
        self.element_hover(self.HOME_LINK)
        home_btn_color_hovered = self.get_value_css(self.HOME_LINK)
        print('Color of hovered button is ' + home_btn_color_hovered)

    def test_product_link(self):
        products_btn_arrow_static = self.get_value_css(self.PRODUCTS_BTN_ARROW, locatorType='xpath', param='background')
        print(f'Background of Products button arror is {products_btn_arrow_static}')
        self.element_hover(self.PRODUCTS_LINK)
        products_btn_hovered = self.get_value_css(self.PRODUCTS_BTN_ARROW, locatorType='xpath', param='background')

        print(f'Background of Products button arror is  {products_btn_hovered}')

    def test_bingo_link(self):
        bingo_btn_color = self.get_value_css(self.BINGO_LINK, locatorType='linktext')
        print('Color of bingo button is ' + bingo_btn_color)
        self.element_hover(self.BINGO_LINK, locatorType='linktext')
        bingo_btn_hovered = self.get_value_css(self.BINGO_LINK, locatorType='linktext')
        print('Color of bingo button is ' + bingo_btn_hovered)

    def test_client_hub_link(self):
        client_hub_btn_color = self.get_value_css(self.CLIENT_HUB, locatorType='xpath')
        print('Color of button is ' + client_hub_btn_color)
        self.element_hover(self.CLIENT_HUB, locatorType='xpath')
        client_hub_btn_color_hovered = self.get_value_css(self.CLIENT_HUB, locatorType='xpath')
        print('Mouse Hovered on element')
        print('Color of hovered button is ' + client_hub_btn_color_hovered)

    def test_company_link(self):
        company_btn_arrow_static = self.get_value_css(self.COMPANY_BTN_ARROW, locatorType='xpath', param='background')
        print(f'Background of Company button arror is {company_btn_arrow_static}')
        self.element_hover(self.COMPANY_LINK, locatorType='linktext')
        company_btn_hovered = self.get_value_css(self.COMPANY_BTN_ARROW, locatorType='xpath', param='background')
        print(f'Background of Company button arror is  {company_btn_hovered}')

    def test_news_link(self):
        news_btn_color = self.get_value_css(self.NEWS_LINK, locatorType='linktext')
        print('Color of button is ' + news_btn_color)
        self.element_hover(self.NEWS_LINK, locatorType='linktext')
        news_btn_color_hovered = self.get_value_css(self.NEWS_LINK, locatorType='linktext')
        print('Mouse Hovered on element')
        print('Color of hovered button is ' + news_btn_color_hovered)

    def test_contact_link(self):
        contact_btn_color = self.get_value_css(self.CONTACT_LINK, locatorType='xpath')
        print('Color of button is ' + contact_btn_color)
        self.element_hover(self.CONTACT_LINK, locatorType='xpath')
        contact_btn_color_hovered = self.get_value_css(self.CONTACT_LINK, locatorType='xpath')
        print('Mouse Hovered on element')
        print('Color of hovered button is ' + contact_btn_color_hovered)


    def test2(self):
        self.element_hover(self.PRODUCTS_LINK)
        self.element_click(self.BINGO_LINK, locatorType='linktext')
