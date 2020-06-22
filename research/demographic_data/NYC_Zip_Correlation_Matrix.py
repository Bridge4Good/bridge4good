import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn

url = 'https://raw.githubusercontent.com/nychealth/coronavirus-data/master/data-by-modzcta.csv'
covid_data_nyc_zips = pd.read_csv(url)

ny_income_by_zip = pd.read_csv('research/demographic_data/ny_income_tax_data_2017.csv')

combined_df = covid_data_nyc_zips.merge(ny_income_by_zip, left_on = "MODIFIED_ZCTA", right_on = "ZIP code [1]")
#data = cases.merge(demos, left_on = "MODZCTA", right_on = "zip")

