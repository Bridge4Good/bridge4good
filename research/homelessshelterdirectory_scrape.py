import bs4
from bs4 import BeautifulSoup
import requests
import pandas as pd

page = requests.get('https://www.homelessshelterdirectory.org/cgi-bin/id/city.cgi?city=New%20York%20City&state=NY')
soup = BeautifulSoup(page.text, features='lxml') #use beautiful soup to parse the html
lst = soup.find_all("div",{"class":"item_content"})

shelters_lst = []
for i in range(1, 111): #only parts with shelters
    shelter = lst[i].text
    shelter = shelter.replace('See more details','')
    shelter = shelter.replace('\n',' ')
    shelter = shelter.replace('\t',' ')
    shelter = shelter.replace('\r',' ')
    shelter = shelter.replace('                    ',' ')
    shelters_lst.append(shelter)
    i += 1

df = pd.DataFrame(shelters_lst)
df.to_csv("homelessshelterdirectory_shelters.csv")

'''
shelters_list = shelters_list[1:111] #getting only shelter

urls = [] 
for a_tag in comment_a_tags:
    url = a_tag['href']
    if not url.startswith('http'):
        url = "https://reddit.com"+url
    urls.append(url)

import bs4
import requests
from bs4 import BeautifulSoup
import time
import matplotlib.pyplot as plt

# In[18]:


def parsePrice(STOCK_NAME):
    r = requests.get("https://finance.yahoo.com/quote/"+STOCK_NAME+"?p="+STOCK_NAME) #returns html of the website
    soup = BeautifulSoup(r.text, 'lxml') #use beautiful soup to parse the html
    price = soup.find_all("div",{"class":"My(6px) Pos(r) smartphone_Mt(6px)"})[0].find("span", {"class": "Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)"}).text #if you look at html code, you see this is where the price can be found
    #price = soup.find_all("div",{"class":"My(6px) Pos(r) smartphone_Mt(6px)"})#.find("span", {"class": "Trsdu(0.3s) Fw(500) Fz(14px) C($positiveColor)"}).text
    #price = soup.find("div",{"class":"My(6px) Pos(r) smartphone_Mt(6px)"}).find("span", {"class": "C(black) Fz(14px) Fw(500)"}).text #for early trading
    return price

 

    
import os
#from IPython.display import clear_output
stock_prices = [] #list of prices that stock was that day
while True:
    price = parsePrice("AMZN").replace(",", '') #replace in case price is >=$1000 and has comma(s)
    stock_prices.append(price)
    #clear_output(wait=True) #clears the output in IPython Console so we can view plot in real time
    os.system('cls')
    plt.plot(stock_prices) #plots stock_prices
    plt.pause(1e-16) #pauses the plot for a bit to allow a new plot to show up
    plt.show()
    time.sleep(1)
'''