# Scraping small businesses in NYC
from bs4 import BeautifulSoup
import requests as req 
import pandas as pd

page = req.get('http://nybizlist.com/nyc-small-business-directory.htm')

soup = BeautifulSoup(page.text, 'lxml')

listings = soup.find_all(class_='featured')

businesses = []
for biz in listings:
    biz = biz.text.replace('\r\n\t\t\t\t\t', '')
    biz = biz.replace('(map)', '').replace('\xa0 |\xa0', '').replace('\n', '')
    businesses.append(biz)

df = pd.DataFrame(businesses)
df.to_csv('nyc_businesses.csv')