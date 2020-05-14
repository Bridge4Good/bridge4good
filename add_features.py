import numpy as np 
import pandas as pd 

data = pd.read_csv("Shelter1_data.csv")
data = data.iloc[:, 3:]
data['Donor Age'] = np.random.randint(18, 100, data.shape[0])
data['Is Volunteer'] = np.random.randint(0, 2, data.shape[0])
data['Salvation Army'] = np.random.randint(0, 2, data.shape[0])
data['New York City Rescue Mission'] = np.random.randint(0, 2, data.shape[0])
data['Covenant House'] = np.random.randint(0, 2, data.shape[0])

print(data.columns)
data.to_csv('donor_data.csv')