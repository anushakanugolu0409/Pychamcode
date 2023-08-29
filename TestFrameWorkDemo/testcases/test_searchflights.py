import pandas as pd
import pytest
from pages.yatra_launch_page import LaunchPage

@pytest.mark.usefixtures("setup")
class TestSearchAndVerifyFilter():
    def test_search_flights(self):
        lp=LaunchPage(self.driver,self.wait)
        lp.departfrom("New Delhi")



dauto=TestSearchAndVerifyFilter()
dauto.test_search_flights()
