import pytest
from selenium import webdriver


@pytest.yield_fixture(scope='class')
def oneTimeSetup(request, browser):
    print('Running one time setUp')
    if browser == 'chrome':
        baseUrl = 'https://courses.letskodeit.com/'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseUrl)
    else:
        baseUrl = 'https://courses.letskodeit.com/'
        driver = webdriver.Firefox()
        print('Running test on firefox')
    if request.cls is not None:
        request.csl.driver = driver
    yield driver
    driver.quit()