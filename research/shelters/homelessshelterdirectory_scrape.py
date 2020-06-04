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
'''