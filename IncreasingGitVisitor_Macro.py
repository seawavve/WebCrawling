

import requests
from selenium import webdriver
import time

for i in range(1):
    driver = webdriver.Chrome('C:/Users/user/Downloads/chromedriver_win32/chromedriver')
    url="https://github.com/seawavve"
    driver.get(url)
    time.sleep(3)
    driver.close()
