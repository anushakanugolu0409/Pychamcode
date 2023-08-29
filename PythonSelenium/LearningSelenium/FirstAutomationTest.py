# Below commented code is used when we manually download the drivers and place in folder
# Webdriver manager is used which will take care of the driver to install and use it in code

"""from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(executable_path="C:\\Browser\\chromedriver.exe" )
driver = webdriver.Chrome(service=service)"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://rcvacademy.com")
driver.maximize_window()
print(driver.title)
driver.close()


