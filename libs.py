# Includes all need imports
# pip install selenium
# pip install webdriver-manager
# 
# import warnings
# warnings.filters('ignore')
# matplotlib inline 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from time import sleep
import selenium
import webdriver_manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options