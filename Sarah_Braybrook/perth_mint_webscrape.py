#Imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
import pandas as pd

import requests
import time
from pprint import pprint

#Setup Driver & Open Webpage
driver = webdriver.Chrome()
url = 'https://www.perthmint.com/'

r = requests.get(url)
r = r.status_code

if r == 200:
    driver.get(url)
    print(f"request code: {r}. Access granted")

    #Setup BeautifulSoup & Parser
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    #Close Cookies
    try:
        cookie_close = driver.find_element(By.ID, "onetrust-reject-all-handler")
        cookie_close.click()
        print("Cookies have successfully been closed")
    except:
        print("No option to authorise cookies")

    #Redirect to Metal Prices
    metal_prices = driver.find_element(By.LINK_TEXT, "View spot prices")
    metal_prices.click()
    print("successfully opened page for Metal Prices")

    #Update BeautifulSoup & Parser
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    #Scrape Metal Prices & Append to Lists
    metals = []
    asks = []
    bids = []

    tables = soup.find_all('div', class_='table__tbody table__tbody--with-header')
    aud_table = tables[0]
    aud_rows = aud_table.find_all('div', class_='table__row u-flex p-2 py-md-3')

    for row in aud_rows:
        cells = row.find_all('span', class_='table__cell mx-md-1 mb-1 mb-md-0')

        metal = cells[0].text.strip()
        ask = cells[1].text.strip()
        bid = cells[2].text.strip()

        metals.append(metal)
        asks.append(ask)
        bids.append(bid)

    #Proceed to "Shop Bullion"
    shop_bullion = driver.find_element(By.LINK_TEXT, "Shop bullion")
    shop_bullion.click()

    #Update BeautifulSoup & Parser
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    #Proceed to "Coins"
    coins = driver.find_element(By.LINK_TEXT, "Coins")
    coins.click()
    print("successfully opened page for Coins")

    #Update BeautifulSoup & Parser
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # #Identify Number of Pages
    # max_pages = driver.find_element(By.CLASS_NAME, "product-list__count")
    # mp_elements = max_pages.find_elements(By.TAG_NAME, "span")
    # max_page = mp_elements[-1].text
    # max_page = int(max_page)

    #Close Browser
    driver.quit()

    #Create DataFrame
    aud_metal_prices = pd.DataFrame(columns=['Metals', 'Ask_Prices', 'Bid_Prices'])

    for i in range(len(metals)):
        data = {'Metals': metals[i], 'Ask_Prices': asks[i], 'Bid_Prices': bids[i]}
        pos = len(aud_metal_prices)
        aud_metal_prices.loc[pos] = data

else:
    print(f"error code: {r}. Unable to access data")
    driver.quit()

aud_metal_prices.to_excel('live_metal_prices.xlsx', index=False)
