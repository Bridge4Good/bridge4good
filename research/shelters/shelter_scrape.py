import pandas as pd 

url = "https://www.shelterlistings.org/city/new_york-ny.html"
city = "nyc"

table = pd.read_html(url)[0]

data = {
    'Name': [],
    'Location': [], 
    'Phone': [],
    'Description': []
}
for row in table[0]:
    row = row.strip('View Full Listing Details')
    row = row.split('  ')

    shelter_name = row[0]
    shelter_location = row[1]
    if len(row) > 2:
        shelter_phone = row[2]
    else:
        shelter_phone = None

    if len(row) > 3:
        shelter_desc = row[3]
    else:
        shelter_desc = None

    data['Name'].append(shelter_name)
    data['Location'].append(shelter_location)
    data['Phone'].append(shelter_phone)
    data['Description'].append(shelter_desc)

df = pd.DataFrame(data)
df.to_csv(city + '_shelters.csv')
print('Done!')


