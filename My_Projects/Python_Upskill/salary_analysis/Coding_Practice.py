import pandas as pd
import matplotlib as mpt
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By

import requests
import time
import classified

driver = webdriver.Chrome()
url = 'https://www.perthmint.com/'

def update_html():
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')


r = requests.get(url)

if r.status_code == 200:
    print("Access Granted")
    driver.get(url)
    update_html
    
    #Essential Cookies Only
    cookie_close = driver.find_element(By.ID, "onetrust-reject-all-handler")
    cookie_close.click()

    
