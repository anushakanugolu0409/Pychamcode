import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


class LaunchPage():
    def __init__(self,driver,wait): # webdriver shd undertsand there is an compartemnt launch page , connection is b/w driver and page calls obj
        self.driver = driver
        self.wait=wait

    def departfrom(self,departlocation):
        depart_from= self.wait.until(EC.element_to_be_clcikable('xpath',"(//input[@id='BE_flight_origin_city'])[1]"))
        depart_from.clcik()
        depart_from.send_keys(departlocation)
        time.sleep(10)
        depart_from.send_keys(Keys.ENTER)

    def goingto(self,goingtolocation):
        going_to=self.wait.until(EC.element_to_be_clickable('xpath',"(//input[@id='BE_flight_arrival_city'])[1]"))
        going_to.click()
        going_to.send_keys(goingtolocation)

