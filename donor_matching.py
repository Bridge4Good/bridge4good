import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn import preprocessing
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics


# Reads and slices CSVs accordingly for x/y inputs for logreg
def csv_cleaner(csv, shelter):
    data = pd.read_csv(csv, header=0)
    data = data.copy().dropna().iloc[:, 1:]
    
    x = data.drop(data.iloc[:, 4:7], axis=1) ## Keeping all except the Y feature
    y = data[shelter] ## Keeping only the Y feature

    return [x, y]

# Shelter 1 Model - Train and test with Shelter1_donor.csv data
def shelter1_logreg():
    data = csv_cleaner('donor_data.csv', 'Salvation Army')
   
    # Split data into train and test randomly
    x1_train, x1_test, y1_train, y1_test = train_test_split(data[0], data[1], test_size=0.3, random_state=0)
    
    # run scikit-learn's builtin logreg
    logreg1 = LogisticRegression(penalty='l2',
        dual=False,
        tol=0.0001,
        C=1.0,
        fit_intercept=True,
        intercept_scaling=1,
        max_iter=1000,
        class_weight=None,
        warm_start=False,
        n_jobs=-1,
        l1_ratio=None)

    # fit the model to the training data
    shelter1_fit = logreg1.fit(x1_train, y1_train)

    # score percentile accuracy of model on test set
    accuracy = 'Accuracy of logistic regression classifier on Shelter 1 test set: {:.2f}'.format(logreg1.score(x1_test, y1_test))

    return shelter1_fit

# Shelter 2 Model - Train and test with Shelter2_donor.csv data
def shelter2_logreg():
    data = csv_cleaner('donor_data.csv', 'New York City Rescue Mission')
  
    # Split data into train and test randomly
    x2_train, x2_test, y2_train, y2_test = train_test_split(data[0], data[1], test_size=0.3, random_state=0)
    
    # run builtin logreg
    logreg2 = LogisticRegression(penalty='l2',
        dual=False,
        tol=0.0001,
        C=1.0,
        fit_intercept=True,
        intercept_scaling=1,
        max_iter=1000,
        class_weight=None,
        warm_start=False,
        n_jobs=-1,
        l1_ratio=None)

    # fit model to training data
    shelter2_fit = logreg2.fit(x2_train, y2_train)

    # score percentile accuracy of model on test set
    accuracy = 'Accuracy of logistic regression classifier on Shelter 2 test set: {:.2f}'.format(logreg2.score(x2_test, y2_test))

    return shelter2_fit

# Shelter 3 Model - Train and test with Shelter3_donor.csv data
def shelter3_logreg():
    data = csv_cleaner('donor_data.csv', 'Covenant House')
    
    # Split data into train and test randomly
    x3_train, x3_test, y3_train, y3_test = train_test_split(data[0], data[1], test_size=0.3, random_state=0)
    
    # run builtin logreg
    logreg3 = LogisticRegression(penalty='l2',
        dual=False,
        tol=0.0001,
        C=1.0,
        fit_intercept=True,
        intercept_scaling=1,
        max_iter=1000,
        class_weight=None,
        warm_start=False,
        n_jobs=-1,
        l1_ratio=None)

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
def match_donor(zipcode, donation, age, volunteer):
    if volunteer.lower() == 'yes':
        volunteer_bin = 1
    elif volunteer.lower() == 'no':
        volunteer_bin = 0
    new_data = [[zipcode, donation, age, volunteer_bin]]
    # Predicting probability that the new_data will have value of 0 ; and probability that it will have a value of 1
    # Splitting arrays into 2 sections (probability of 0 and probability of 1)
    # Getting final % match data
    shelter1 = match_percent(np.split(shelter1_logreg().predict_proba(new_data)[0], indices_or_sections=2)[1])
    shelter2 = match_percent(np.split(shelter2_logreg().predict_proba(new_data)[0], indices_or_sections=2)[1])
    shelter3 = match_percent(np.split(shelter3_logreg().predict_proba(new_data)[0], indices_or_sections=2)[1])

    # storing shelters in a dictionary to find the key of the highest % match
    shelters = {'Salvation Army': shelter1, 
                'New York City Rescue Mission': shelter2, 
                'Covenant House': shelter3}
    final_shelter = max(shelters, key=shelters.get)
    final_shelter_match = shelters[final_shelter]
    
    message = 'Based on your input, we recommend that you donate to the %s shelter for which you are a %s!' % (final_shelter, final_shelter_match)

    return message
