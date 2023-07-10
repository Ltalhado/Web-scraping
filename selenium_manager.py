# Includes all need imports
# pip install selenium
# pip install webdriver-manager
#
# import warnings
# warnings.filters('ignore')
# matplotlib inline
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options = webdriver.ChromeOptions()
# options.add_argument("headless")
options.add_argument("--disable-gpu'")
driver = webdriver.Chrome()
# executable_path='/Users/${userName}/Drivers/chromedriver', chrome_options=options)
