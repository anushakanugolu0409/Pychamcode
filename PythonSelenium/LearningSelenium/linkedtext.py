from selenium import webdriver
import time


class DemoFindEleBylink():
    def loc_by_link(self):
        driver = webdriver.Chrome()
        driver.get("https://www.flipkart.com//")
        time.sleep(10)
        driver.find_element('link text','Bluetooth Headphones').click()



f = DemoFindEleBylink()
f.loc_by_link()
