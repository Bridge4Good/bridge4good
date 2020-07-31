import pandas as pd
import numpy as np
import plotly.express as px

def read_and_filter_data():
    #Reading and filtering 2015 Donation data
        #Value Category = All - # donating to charity (2013-2015), Percent Donating $25.00 or more (2015) (and for individual years 2008-5)
    donations = pd.read_csv("AI_for_Social_Good/Volunteering_and_Civic_Life_in_America.csv")
    percent_donating_25_dollars_or_more = donations.loc[donations['Value Category'] == 'All - % donating to charity (2013-2015)']
    #percent_donating_2013_to_15 = donations.loc[donations['Value Category'] == 'All - % donating to charity (2013-2015)']

    #Reading and filtering 2018 SAIPE data
    poverty_and_income = pd.read_excel("AI_for_Social_Good/SAIPE_State_and_County_Estimates_2018.xls")
    poverty_and_income = poverty_and_income[1:]

    #Reading and filtering 2019 homelessness data
    homelessness = pd.read_excel("AI_for_Social_Good/2019-PIT-Counts-by-State.xlsx")

    #Reading and filtering 2019 HIC (housing) data
    beds = pd.read_excel('AI_for_Social_Good/2019-HIC-Counts-by-State.xlsx')

    return percent_donating_25_dollars_or_more, poverty_and_income, homelessness, beds

def combine_data():
    percent_donating_25_dollars_or_more, poverty_and_income, homelessness, beds = read_and_filter_data()
    
    #Merging data
    master_df = percent_donating_25_dollars_or_more.merge(poverty_and_income, left_on = 'Location Name', right_on = 'Name')
    master_df = master_df.merge(homelessness, left_on = 'Postal Code', right_on = 'State')
    master_df = master_df.merge(beds, left_on = 'Postal Code', right_on = 'State')
    
    #Extracting columns and renaming them
    master_df = master_df[['Location Name', 'Postal Code', 'METRIC', 
            'Poverty Percent, All Ages', 'Overall Homeless, 2019', 'Median Household Income', 'Total Year-Round Beds (ES, TH, SH)']]
            #Emergency Shelter (ES), Transitional Housing (TH), Safe Haven (SH)
    master_df.rename(columns={'Location Name':'State', 'Postal Code':'State Abbreviation', 
            'METRIC':'All - % donating to charity (2013-2015)', 'Poverty Percent, All Ages': 'Poverty Percent, All Ages (2018)',
            'Total Year-Round Beds (ES, TH, SH)':'Total Year-Round Beds'}, inplace=True)
    
    return master_df

#Creating plots

def plots_with_labeled_points():
    master_df = combine_data()

    donations_vs_overallhomelessness_fig = px.scatter(master_df, x="All - % donating to charity (2013-2015)", y="Overall Homeless, 2019", color="State",
            hover_data=['All - % donating to charity (2013-2015)', 'Overall Homeless, 2019'])
    donations_vs_overallhomelessness_fig.update_layout(title="Donations vs Overall Homelessness")
    donations_vs_overallhomelessness_fig.show()

    donations_vs_poverty_fig = px.scatter(master_df, x="All - % donating to charity (2013-2015)", y="Poverty Percent, All Ages (2018)", color="State",
            hover_data=['All - % donating to charity (2013-2015)', 'Poverty Percent, All Ages (2018)'])
    donations_vs_poverty_fig.update_layout(title="Donations vs Poverty Percent")
    donations_vs_poverty_fig.show()

    '''
    donations_vs_income_fig = px.scatter(master_df, x="All - % donating to charity (2013-2015)", y="Median Household Income", color="State",
        hover_data=['All - % donating to charity (2013-2015)', 'Median Household Income'])
    donations_vs_income_fig.update_layout(title="Donations vs Income")
    donations_vs_income_fig.show()
    '''

#plots_with_labeled_points()

def plots_with_trendlines():
    master_df = combine_data()

    donations_vs_overallhomelessness_trendlinefig = px.scatter(master_df, x="All - % donating to charity (2013-2015)", y="Overall Homeless, 2019", 
            hover_data=['All - % donating to charity (2013-2015)', 'Overall Homeless, 2019'], trendline='ols')
    donations_vs_overallhomelessness_trendlinefig.update_layout(title="Donations vs Overall Homelessness (Trendline)")
    donations_vs_overallhomelessness_trendlinefig.show()

    donations_vs_poverty_trendlinefig = px.scatter(master_df, x="All - % donating to charity (2013-2015)", y="Poverty Percent, All Ages (2018)", 
            hover_data=['All - % donating to charity (2013-2015)', 'Poverty Percent, All Ages (2018)'], trendline='ols')
    donations_vs_poverty_trendlinefig.update_layout(title="Donations vs Poverty Percent (Trendline)")
    donations_vs_poverty_trendlinefig.show()
    
    '''
    donations_vs_income_trendlinefig = px.scatter(master_df, x="All - % donating to charity (2013-2015)", y="Median Household Income", 
        hover_data=['All - % donating to charity (2013-2015)', 'Median Household Income'], trendline='ols')
    donations_vs_income_trendlinefig.update_layout(title="Donations vs Income")
    donations_vs_income_trendlinefig.show()
    '''

#plots_with_trendlines()

def beds_vs_homelessness():
    master_df = combine_data()
    
    #labeled points figure
    beds_vs_homelessness_fig = px.scatter(master_df, x="Total Year-Round Beds", y="Overall Homeless, 2019", color="State",
            hover_data=['Total Year-Round Beds', 'Overall Homeless, 2019'])
    beds_vs_homelessness_fig.update_layout(title="Total Beds vs Overall Homelessness")
    beds_vs_homelessness_fig.show()

    #trendline figure
    beds_vs_homelessness_trendlinefig = px.scatter(master_df, x="Total Year-Round Beds", y="Overall Homeless, 2019", 
            hover_data=['Total Year-Round Beds', 'Overall Homeless, 2019'], trendline='ols')
    beds_vs_homelessness_trendlinefig.update_layout(title="Total Beds vs Overall Homelessness (Trendline)")
    beds_vs_homelessness_trendlinefig.show()

beds_vs_homelessness()