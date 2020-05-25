# Consolidating our list of charities/shelters helping the homeless
# I'm also adding an additional article from which I'm scraping
from bs4 import BeautifulSoup
import requests as req 
import pandas as pd 

r = req.get('https://www.timeout.com/newyork/things-to-do/where-to-volunteer-homelessness')

soup = BeautifulSoup(r.text, 'lxml')
charities = soup.find('article')

titles = charities.find_all(class_='title-underline theme-title-underline-static')
descs = charities.find_all('p')
descs = descs[4:len(descs) - 4]

data = {
    'Name': [title.text.strip() for title in titles],
    'Location': [],
    'Phone': [],
    'Website': [],
    'Description': []
}

for desc in descs:

    # splitting to parse out categories
    item = desc.text.split('. ')

    # removing the volunteer requests
    if "to volunteer" in item[len(item) - 1]:
        item.remove(item[len(item) - 1])
       
    contact = item[len(item) - 1].split('(')

    # Getting location, phone, website
    if len(contact) == 2:
        location = contact[0].strip()
        info = contact[1].split(',')
        
        phone = info[0].strip(')').strip()

        if len(info) == 2:
            website = info[1].strip(')').strip()
        else:
            website = ''

    else:
        location = ''
        info = contact[0].split(' ')
        phone = info[1].strip()
        website = info[4].strip('.').strip()

    description = ' '.join(item[0:len(item) - 2])

    data['Location'].append(location)
    data['Phone'].append(phone)
    data['Website'].append(website)
    data['Description'].append(description)

# Adding data to csv
'''
df = pd.DataFrame(data)
add_df = pd.read_csv('./research/nyc_shelters.csv')
add_df['Website'] = ''

final = pd.concat([df, add_df], axis=0)
final.to_csv('charities.csv')
'''

# cleaning up csv
chars = pd.read_csv('charities.csv')
chars = chars.loc[:, 'Name':'Description']
chars.to_csv('charities.csv')