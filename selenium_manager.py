# Includes all need imports
# pip install selenium
# pip install webdriver-manager
#
# import warnings
# warnings.filters('ignore')
# matplotlib inline

# import selenium
# import webdriver_manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome(
    executable_path='/Users/${userName}/Drivers/chromedriver', chrome_options=options)
