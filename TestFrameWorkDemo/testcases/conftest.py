import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

@pytest.fixture(scope='class')
def setup(request):
    driver= webdriver.Chrome()
    wait=WebDriverWait(driver,10)
    driver.get("https://www.yatra.com/")
    driver.maximize_window()
    request.cls.driver = driver  # driver shd be avilable to the "cls" is class which is requesting for the driver
    request.cls.driver=wait
    yield
    driver.close()
