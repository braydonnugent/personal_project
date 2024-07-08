import pandas as pd
import matplotlib as mpt
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import requests
import time

url = "https://www.sportsbet.com.au/betting/ufc-mma/ufc-matches"
r = requests.get(url)

if r.status_code == 200:
    print("Access Granted!")
    driver = webdriver.Chrome()
    driver.get(url)

    try:
        #Initialise html
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        try:
            futures = driver.find_elements(By.CLASS_NAME, 'tabTouchable_f14y21fs')
            future = futures[-1]
        finally:
            future.click()
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            print("Clicked 'future' successfully")

        group_a = soup.find_all('div', class_='outcomeName_f1lx8d3l textWrap_fofl8s outcomeDetailsFirst_fj7k5vv twoOutcomes_f1jesm74')
        group_b = soup.find_all('div', class_='outcomeName_f1lx8d3l textWrap_fofl8s outcomeDetailsLast_fu8m1aj twoOutcomes_f1jesm74')
        odds = soup.find_all('div', class_='priceText_f71sibe')
        
    finally:
        driver.close()

    a_side = []
    b_side = []
    odds_a = []
    odds_b = []

    for a in group_a:
        fighter = a.text.replace(' ', '_')
        a_side.append(fighter)

    for b in group_b:
        fighter = b.text.replace(' ', '_')
        b_side.append(fighter)

    sep = 2

    for i in range(len(odds)):
        bet = odds[i].text
        if i % sep == 0:
            odds_a.append(bet)
        else:
            odds_b.append(bet)

    mma_fights = pd.DataFrame(columns=['Fighter_A', 'Odds_A', 'Fighter_B', 'Odds_B'])

    for i in range(len(a_side)):
        fight = {'Fighter_A': a_side[i], 'Odds_A': odds_a[i], 'Fighter_B': b_side[i], 'Odds_B': odds_b[i]}
        
        new_index = len(mma_fights)
        mma_fights.loc[new_index] = fight

    print(mma_fights)

else:
    print(f"Access Denied! Error Code: {r.status_code}.")

