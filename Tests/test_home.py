import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from Pages.home import HomePage


class TestHome():

    def test1(self):
        baseUrl = 'https://www.pragmaticplay.com/en/'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)
        hp = HomePage(driver)

        hp.close_home_popup()
        hp.test_home_link()
        hp.test_product_link()
        hp.test_bingo_link()
        hp.test_client_hub_link()
        hp.test_company_link()
        hp.test_news_link()
        hp.test_contact_link()


# cc = TestHome()
# cc.test1()
