import pandas as pd
import numpy as np
import plotly.express as px

#Reading and filtering 2015 Donation data
#Value Category = All - # donating to charity (2013-2015), Percent Donating $25.00 or more (2015) (and for individual years 2008-5)
donations_by_state = pd.read_csv("AI_for_Social_Good/Volunteering_and_Civic_Life_in_America.csv")
percent_donating_25_dollars_or_more = donations_by_state.loc[donations_by_state['Value Category'] == 'Percent Donating $25.00 or more (2015)']
#percent_donating_2013_to_15 = donations_by_state.loc[donations_by_state['Value Category'] == 'All - % donating to charity (2013-2015)']

#Reading and filtering 2015 SAIPE data
poverty_and_income_by_state = pd.read_excel("AI_for_Social_Good/SAIPE_State_and_County_Estimates_2015.xls")
poverty_and_income_by_state = poverty_and_income_by_state[1:]

#Reading and filtering 2015 homelessness data
homelessness_by_state = pd.read_excel("AI_for_Social_Good/2015-PIT-Counts-by-State.xlsx")

#Combining data
master_df = percent_donating_25_dollars_or_more.merge(poverty_and_income_by_state, left_on = 'Location Name', right_on = 'Name')
master_df = master_df.merge(homelessness_by_state, left_on = 'Postal Code', right_on = 'State')
master_df = master_df[['Location Name', 'Postal Code', 'METRIC', 'Poverty Estimate, All Ages', 
'Poverty Percent, All Ages', 'Median Household Income', 'Overall Homeless, 2015']]
#Overall Homeless - Black or African American, 2015
master_df.rename(columns={'Location Name':'State', 'Postal Code':'State Abbreviation', 
'METRIC':'Percent Donating $25.00 or more (2015)', 'Poverty Percent, All Ages': 'Poverty Percent, All Ages (2015)'}, inplace=True)

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