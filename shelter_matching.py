import pandas as pd
import numpy as np

from sklearn import preprocessing
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.model_selection import GridSearchCV

# ## Shelter 1 Model - Train and test with donor_data
def csv_cleaner(csv, shelter):
    data = pd.read_csv(csv, header=0)
    data = data.copy().dropna().iloc[:, 1:]
    
    return data

def generate_xy(shelter):
    data = csv_cleaner("donor_data.csv", shelter)

    x1 = data.drop(data.iloc[:, 5:8], axis=1) ## Keeping all except the Y feature
    y1 = data[shelter] ## Keeping only the Y feature

    x1_train, x1_test, y1_train, y1_test = train_test_split(x1, y1, test_size=0.3, random_state=0)
    
    return x1_train, x1_test, y1_train, y1_test

### Logistic Regression
def logreg(shelter):
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

    data = generate_xy(shelter)

    fitted = logreg1.fit(data[0], data[2])
   
    # y1_pred = fitted.predict(data[1])
    # accuracy = 'Accuracy of logistic regression classifier on Shelter 1 test set: {:.2f}'.format(logreg1.score(data[1], data[3]))
    
    ## Getting the probability value out for each of the test customers
    y1_pred_prob = fitted.predict_proba(np.array(data[1]))
    
    return y1_pred_prob

def test_logreg(shelter):
    y1_pred_prob = logreg(shelter)
    data = generate_xy(shelter)
    shelter_data = csv_cleaner("donor_data.csv", shelter)

    ### Creating a test data for checking our results
    testData = shelter_data.loc[data[3]]
    testData["Probability"] = 0.0

    testData.Probability = y1_pred_prob

    return testData


def topthree(shelter):
    testData = test_logreg(shelter)
    testData = testData.sort_values(["Probability"],ascending=False)
    top3 = testData.head(3)[['Donor Zip', 'Donor Budget', 'Donor Age', 'Is Volunteer', 'Probability']]
    top3 = top3.to_html(index=False)

    message = 'Here is the information for the top 3 potential donors to your shelter: ' + '\n'
    
    return message, top3
