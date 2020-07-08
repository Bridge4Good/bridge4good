import pandas as pd
import numpy as np
import plotly.express as px

#Reading and filtering 2015 Donation data
donations = pd.read_csv("AI_for_Social_Good/Volunteering_and_Civic_Life_in_America.csv")
percent_donating_25_dollars_or_more = donations.loc[donations['Value Category'] == 'Percent Donating $25.00 or more (2015)']

#Reading and filtering 2015 SAIPE data
poverty_and_income = pd.read_excel("AI_for_Social_Good/SAIPE_State_and_County_Estimates_2015.xls")
poverty_and_income = poverty_and_income[1:]

#Reading and homelessness data
homelessness = pd.read_excel("AI_for_Social_Good/2015-PIT-Counts-by-State.xlsx")
#Reading population data
population = pd.read_excel("AI_for_Social_Good/Annual_Estimates_Resident_Population.xlsx")

#Combining data
master_df = percent_donating_25_dollars_or_more.merge(poverty_and_income, left_on = 'Location Name', right_on = 'Name')
master_df = master_df.merge(population, left_on = 'Location Name', right_on = 'Geographic Area')
master_df = master_df.merge(homelessness, left_on = 'Postal Code', right_on = 'State')
master_df = master_df[['Location Name', 'METRIC', 'Poverty Estimate, All Ages', 
'Poverty Percent, All Ages', 'Overall Homeless, 2015', 2015]] #'Postal Code', 'Median Household Income'
#Overall Homeless - Black or African American, 2015
master_df.rename(columns={'Location Name':'State', 'Postal Code':'State Abbreviation', 
'METRIC':'Percent Donating $25.00 or more (2015)', 'Poverty Percent, All Ages': 'Poverty Percent, All Ages (2015)', 2015: 'Total Population (2015'}, inplace=True)
master_df['Total Number of Donors (2015)'] = master_df['Percent Donating $25.00 or more (2015)'] * master_df['Total Population (2015']
master_df = master_df[['State', 'Total Number of Donors (2015)', 'Poverty Percent, All Ages (2015)', 'Overall Homeless, 2015']]

print("Making plots with labeled points")
donations_vs_overallhomelessness_fig = px.scatter(master_df, x="Total Number of Donors (2015)", y="Overall Homeless, 2015", color="State",
    hover_data=['Total Number of Donors (2015)', 'Overall Homeless, 2015'])
donations_vs_overallhomelessness_fig.update_layout(title="2015--Donations vs Overall Homelessness", xaxis_type="log")

donations_vs_poverty_fig = px.scatter(master_df, x="Total Number of Donors (2015)", y="Poverty Percent, All Ages (2015)", color="State",
    hover_data=['Total Number of Donors (2015)', 'Poverty Percent, All Ages (2015)'])
donations_vs_poverty_fig.update_layout(title="2015--Donations vs Poverty Percent", xaxis_type="log")

donations_vs_overallhomelessness_fig.show()
donations_vs_poverty_fig.show()

print("Making plots with trend lines")
donations_vs_overallhomelessness_trendlinefig = px.scatter(master_df, x="Total Number of Donors (2015)", y="Overall Homeless, 2015", 
    hover_data=['Total Number of Donors (2015)', 'Overall Homeless, 2015'], trendline='ols')
donations_vs_overallhomelessness_trendlinefig.update_layout(title="2015--Donations vs Overall Homelessness (Trendline)", xaxis_type="log")

donations_vs_poverty_trendlinefig = px.scatter(master_df, x="Total Number of Donors (2015)", y="Poverty Percent, All Ages (2015)", 
    hover_data=['Total Number of Donors (2015)', 'Poverty Percent, All Ages (2015)'], trendline='ols')
donations_vs_poverty_trendlinefig.update_layout(title="2015--Donations vs Poverty Percent (Trendline)", xaxis_type="log")

donations_vs_overallhomelessness_trendlinefig.show()
donations_vs_poverty_trendlinefig.show()
'''
#Making plots with labeled points
donations_vs_overallhomelessness_fig = px.scatter(master_df, x="Percent Donating $25.00 or more (2015)", y="Overall Homeless, 2015", color="State",
    hover_data=['Percent Donating $25.00 or more (2015)', 'Overall Homeless, 2015'])
donations_vs_overallhomelessness_fig.update_layout(title="2015--Donations vs Overall Homelessness")

donations_vs_poverty_fig = px.scatter(master_df, x="Percent Donating $25.00 or more (2015)", y="Poverty Percent, All Ages (2015)", color="State",
    hover_data=['Percent Donating $25.00 or more (2015)', 'Poverty Percent, All Ages (2015)'])
donations_vs_poverty_fig.update_layout(title="2015--Donations vs Poverty Percent")

donations_vs_overallhomelessness_fig.show()
donations_vs_poverty_fig.show()

#Making plots with trend lines
donations_vs_overallhomelessness_trendlinefig = px.scatter(master_df, x="Percent Donating $25.00 or more (2015)", y="Overall Homeless, 2015", 
    hover_data=['Percent Donating $25.00 or more (2015)', 'Overall Homeless, 2015'], trendline='ols')
donations_vs_overallhomelessness_trendlinefig.update_layout(title="2015--Donations vs Overall Homelessness (Trendline)")

donations_vs_poverty_trendlinefig = px.scatter(master_df, x="Percent Donating $25.00 or more (2015)", y="Poverty Percent, All Ages (2015)", 
    hover_data=['Percent Donating $25.00 or more (2015)', 'Poverty Percent, All Ages (2015)'], trendline='ols')
donations_vs_poverty_trendlinefig.update_layout(title="2015--Donations vs Poverty Percent (Trendline)")

donations_vs_overallhomelessness_trendlinefig.show()
donations_vs_poverty_trendlinefig.show()
'''