import requests
from requests_html import HTMLSession

import pandas as pd


fighters = ['Alexander_Volkanovski', 'Robert_Whittaker']

try:
    session = HTMLSession()
    
    for fighter in fighters:

        url = f'https://en.wikipedia.org/wiki/{fighter}'
        
        attempts = 0
        valid_page = False

        while not valid_page:
            response = session.get(url)
            tables = response.html.find('table.wikitable')

            if len(tables) >= 2:
                valid_page = True
                record = tables[0]
                history = tables[1]

            else:
                url = f'https://en.wikipedia.org/wiki/{fighter}_(fighter)'
                attempts += 1

            if attempts == 2:
                print(f"Too many attempts finding page for {fighter}.")
                record = "N/A"
                history = "N/A"
                break
                
    
    stats = []

    if 'history' in locals():
        items = history.find('td')
        rows = len(history.find('tr'))
        
        for item in items:
            stat = item.text.strip()
            stats.append(stat)

        print(stats[0], stats[1], stats[2], stats[3], stats[4], stats[5], stats[6], stats[7], stats[8], stats[9])

        
        

except requests.exceptions.RequestException as e:
    print(e)

