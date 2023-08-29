import requests
from bs4 import BeautifulSoup
import pandas as pd

response= requests.get("https://www.xelplus.com/all-tutorials/")
print(response.status_code)
print(response.text)
