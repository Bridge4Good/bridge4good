import numpy as np 
import pandas as pd 

data = pd.read_csv("Shelter1_data.csv")

data['Donor Age'] = np.random.randint(18, 100, data.shape[0])
data['Is Volunteer'] = np.random.randint(0, 2, data.shape[0])
data['Tax Rate'] = np.random.choice([0.10, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37], data.shape[0])
data['Months Since Last Donation'] = np.random.randint(0, 20, data.shape[0])
data['Shelter 1'] = np.random.randint(0, 2, data.shape[0])
data['Shelter 2'] = np.random.randint(0, 2, data.shape[0])
data['Shelter 3'] = np.random.randint(0, 2, data.shape[0])

data.to_csv('donor_data.csv')