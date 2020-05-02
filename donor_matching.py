import pandas as pd
import numpy as np

from sklearn import preprocessing
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics


# Reads and slices CSVs accordingly for x/y inputs for logreg
def csv_cleaner(csv):
    data = pd.read_csv(csv, header=0)
    data = data.dropna()

    x = data.iloc[:, 0:2].values
    y = data.iloc[:, 2].values

    return x, y

# Shelter 1 Model - Train and test with Shelter1_donor.csv data
def shelter1_logreg():
    data = csv_cleaner('Shelter1_donor.csv')

    # Split data into train and test randomly
    x1_train, x1_test, y1_train, y1_test = train_test_split(data[0], data[1], test_size=0.3, random_state=0)
    
    # run scikit-learn's builtin logreg
    logreg1 = LogisticRegression()

    # fit the model to the training data
    shelter1_fit = logreg1.fit(x1_train, y1_train)

    # score percentile accuracy of model on test set
    accuracy = 'Accuracy of logistic regression classifier on Shelter 1 test set: {:.2f}'.format(logreg1.score(x1_test, y1_test))

    return shelter1_fit

# Shelter 2 Model - Train and test with Shelter2_donor.csv data
def shelter2_logreg():
    data = csv_cleaner('Shelter2_donor.csv')
  
    # Split data into train and test randomly
    x2_train, x2_test, y2_train, y2_test = train_test_split(data[0], data[1], test_size=0.3, random_state=0)
    
    # run builtin logreg
    logreg2 = LogisticRegression()

    # fit model to training data
    shelter2_fit = logreg2.fit(x2_train, y2_train)

    # score percentile accuracy of model on test set
    accuracy = 'Accuracy of logistic regression classifier on Shelter 2 test set: {:.2f}'.format(logreg2.score(x2_test, y2_test))

    return shelter2_fit

# Shelter 3 Model - Train and test with Shelter3_donor.csv data
def shelter3_logreg():
    data = csv_cleaner('Shelter3_donor.csv')
    
    # Split data into train and test randomly
    x3_train, x3_test, y3_train, y3_test = train_test_split(data[0], data[1], test_size=0.3, random_state=0)
    
    # run builtin logreg
    logreg3 = LogisticRegression()

    # fit model to data
    shelter3_fit = logreg3.fit(x3_train, y3_train)
    
    # score percentile accuracy of model on test set
    accuracy = 'Accuracy of logistic regression classifier on Shelter 3 test set: {:.2f}'.format(logreg3.score(x3_test, y3_test))
    
    return shelter3_fit

# Get "___% match" from probability values
def match_percent(proba):
    percent = proba[0] * 100
    percent_per_outcome = str(percent).lstrip('[').rstrip(']').split(' ')
    percent_per_outcome = list(filter(None, percent_per_outcome))
    
    match =  round(float(percent_per_outcome[1]), 2)

    return str(match) + '% match'

# Run logreg on new user input; print 3 probabilities; match donor with the shelter with highest % match 
def match_donor(zipcode, donation):
    new_data = [[zipcode, donation]]

    # Predicting probability that the new_data will have value of 0 ; and probability that it will ahve a value of 1
    # Splitting arrays into 2 sections
    # Getting final % match data
    shelter1 = match_percent(shelter1_logreg().predict_proba(new_data))
    shelter2 = match_percent(shelter2_logreg().predict_proba(new_data))
    shelter3 = match_percent(shelter3_logreg().predict_proba(new_data))

    # storing shelters in a dictionary to find the shelter of the highest % match
    shelters = {'Salvation Army': shelter1, 
                'Covenant House': shelter2, 
                'New York City Rescue Mission': shelter3}

    final_shelter = max(shelters, key=shelters.get)
    final_shelter_match = shelters[final_shelter]
    
    message = 'Based on your input, we recommend that you donate to the %s shelter for which you are a %s!' % (final_shelter, final_shelter_match)

    return message
