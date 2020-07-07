import pandas as pd
import numpy as np

#Reading and filtering Donation data
#Value Category = All - # donating to charity (2013-2015), Percent Donating $25.00 or more (2015) (and for individual years 2008-5)
donations_by_state = pd.read_csv("AI_for_Social_Good/Volunteering_and_Civic_Life_in_America.csv")
percent_donating_25_dollars_or_more_2015 = donations_by_state.loc[donations_by_state['Value Category'] == 'Percent Donating $25.00 or more (2015)']
percent_donating_25_dollars_or_more_2015 = percent_donating_25_dollars_or_more_2015.reset_index()
percent_donating_2013_to_15 = donations_by_state.loc[donations_by_state['Value Category'] == 'All - % donating to charity (2013-2015)']
percent_donating_2013_to_15 = percent_donating_2013_to_15.reset_index()

#Reading and filtering SAIPE data
poverty_and_income_by_state = pd.read_excel("AI_for_Social_Good/SAIPE_State_and_County_Estimates_2015.xls")
poverty_and_income_by_state = poverty_and_income_by_state[1:]
poverty_and_income_by_state = poverty_and_income_by_state.reset_index()
print(poverty_and_income_by_state)

#Reading and filtering homelessness data
