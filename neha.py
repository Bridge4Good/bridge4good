import pandas as pd

import numpy as np

from sklearn import preprocessing

import matplotlib.pyplot as plt

plt.rc("font", size=14)

from sklearn.feature_selection import RFE

from sklearn.linear_model import LogisticRegression

from sklearn.model_selection import train_test_split

from sklearn import metrics

import seaborn as sns

sns.set(style="white")

sns.set(style="whitegrid", color_codes=True)

# Shelter 1 Model - Train and test with Shelter1_donor.csv data

shelter1data = pd.read_csv('Shelter1_donor.csv',header=0)

shelter1data = shelter1data.dropna()

x1 = shelter1data.iloc[:, 0:2].values 

y1 = shelter1data.iloc[:, 2].values 

#print(shelter1data.head(5))

x1_train, x1_test, y1_train, y1_test = train_test_split(x1, y1, test_size=0.3, random_state=0)

logreg1 = LogisticRegression()

shelter1result = logreg1.fit(x1_train, y1_train)

print(shelter1result)
 
y1_pred = logreg1.predict(x1_test)

print('Accuracy of logistic regression classifier on Shelter 1 test set: {:.2f}'.format(logreg1.score(x1_test, y1_test)))

# Shelter 2 Model - Train and test with Shelter2_donor.csv data

shelter2data = pd.read_csv('Shelter2_donor.csv',header=0)

shelter2data = shelter2data.dropna()

x2 = shelter2data.iloc[:, 0:2].values 

y2 = shelter2data.iloc[:, 2].values 

#print(shelter2data.head(5))

x2_train, x2_test, y2_train, y2_test = train_test_split(x2, y2, test_size=0.3, random_state=0)

logreg2 = LogisticRegression()

shelter2result = logreg2.fit(x2_train, y2_train)

print(shelter2result)
 
y2_pred = logreg2.predict(x2_test)

print('Accuracy of logistic regression classifier on Shelter 2 test set: {:.2f}'.format(logreg2.score(x2_test, y2_test)))

# Shelter 3 Model - Train and test with Shelter3_donor.csv data

shelter3data = pd.read_csv('Shelter3_donor.csv',header=0)

shelter3data = shelter3data.dropna()

x3 = shelter3data.iloc[:, 0:2].values 

y3 = shelter3data.iloc[:, 2].values 

#print(shelter3data.head(5))

x3_train, x3_test, y3_train, y3_test = train_test_split(x3, y3, test_size=0.3, random_state=0)

logreg3 = LogisticRegression()

shelter3result = logreg3.fit(x3_train, y3_train)

print(shelter3result)
 
y3_pred = logreg3.predict(x3_test)

print('Accuracy of logistic regression classifier on Shelter 3 test set: {:.2f}'.format(logreg3.score(x3_test, y3_test)))

# User Interface 
option = input (" Thank you for choosing to donate to the homeless in these desperate times of Covid! Please enter 1 if you are a donor , 2 if you are a homeless shelter")

op = int(option)
if op == 1: 
 donor = input (" THANK YOU, donor! Please enter your zipcode  ")
 amount = input (" Please enter amount you would like to donate!  ")
 #shelter1 = logreg1.predict(
 #shelter2 = logreg2.predict(
 #shelter3 = logreg3.predict(
 #Print the 3 probabilities and the answer is the one with the highest probability
 print('Probability of Shelter 1: , Probability of Shelter 2, Probability of Shelter 3')
 print('Congrats Donor! Based off your location, we recommend that you donate to _______')
elif op == 2: 
 shelter = input (" THANK YOU, for everything you do for the homeless! Please enter your assigned shelter number  ")
else:
 print('Oops,You entered an incorrect choice! ')    
