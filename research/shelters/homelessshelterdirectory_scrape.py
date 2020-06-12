import bs4
from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.homelessshelterdirectory.org/cgi-bin/id/city.cgi?city=Atlanta&state=GA"
city = "atlanta"

page = requests.get(url=url)

soup = BeautifulSoup(page.text, features='lxml') #use beautiful soup to parse the html
lst = soup.find_all("div",{"class":"item_content"})

shelters_lst = []
for shelter in lst:
    shelter = shelter.text
    shelter = shelter.replace('See more details','')
    shelter = shelter.replace('\n',' ')
    shelter = shelter.replace('\t',' ')
    shelter = shelter.replace('\r',' ')
    shelter = shelter.replace('                    ',' ')
    shelters_lst.append(shelter)

df = pd.DataFrame(shelters_lst)
df.to_csv("homelessshelterdirectory_" + city + "_shelters.csv")

'''
shelters_list = shelters_list[1:111] #getting only shelter

urls = [] 
for a_tag in comment_a_tags:
    url = a_tag['href']
    if not url.startswith('http'):
        url = "https://reddit.com"+url
    urls.append(url)
'''