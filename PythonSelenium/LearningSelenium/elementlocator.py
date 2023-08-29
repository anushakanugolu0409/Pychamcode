from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

class DemoFindEleById():
    def loc_by_id(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/register")
        driver.find_element('id',"login-input").send_keys("test@test.com")
        time.sleep(4)
findbyid = DemoFindEleById()
findbyid.loc_by_id()
