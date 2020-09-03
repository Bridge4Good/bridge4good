import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn

'''
ny_income_by_zip = pd.read_csv('/Users/victoriali/Documents/GitHub/bridge4good/research/demographic_data/ny_income_tax_data_2017.csv')

def countydata(county):
  totaldata = all_covid_data()
  onecounty = totaldata.loc[totaldata['county'] == county]
  onecounty = onecounty.reset_index(drop = True)

  return onecounty
'''
#cleaning up nyt covid data by state and date
def all_covid_data():
    url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'
    totaldata = pd.read_csv(url)

    return totaldata

def countydata_state(state):
    totaldata = all_covid_data()
    onestate = totaldata.loc[totaldata['state'] == state]
    onestate = onestate.reset_index(drop = True)

    return onestate

def countydata_state_and_date(state, date):
    all_dates = countydata_state(state)
    onedate = all_dates.loc[all_dates['date'] == date]
    onedate = onedate.reset_index(drop = True)

    return onedate

#final cleaned up data by state and date
ny_covid_by_county = countydata_state_and_date('New York', '2020-06-21')

#importing 2018 income data (by county)
ny_income_by_county = pd.read_excel('research/demographic_data/ny_income_by_county_2018.xlsx')

#combining dataframes
combined_df = ny_covid_by_county.merge(ny_income_by_county)
combined_df = combined_df.drop(columns=['state', 'date', 'county'])
#print(combined_df)

#creating a correlation matrix
corrMatrix = combined_df.corr()
#print(corrMatrix)
sn.heatmap(corrMatrix, annot=True)
plt.show()