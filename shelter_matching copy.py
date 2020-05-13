import pandas as pd
import numpy as np

from sklearn import preprocessing
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.model_selection import GridSearchCV

# ## Shelter 1 Model - Train and test with donor_data
def csv_cleaner(csv):
    data = pd.read_csv(csv, header=0)
    data = data.copy().dropna()
    
    ### To effectively capture the effect of city and state , you need to one-hot-encode it. That is convert the state/city column to a binary variable
    data = pd.get_dummies(data, columns = ["Donor City", "Donor State"])
    ### Removing Zip as this is redundant information, unless you are capturing the distance between the shelter and the customer using this. 
    data = data.iloc[:,2:]
    
    return data

def generate_xy_shelter1():
    data = csv_cleaner("donor_data.csv")
    x1 = data.drop(["Shelter 1", "Shelter 2", "Shelter 3"], axis = 1) ## Keeping all except the Y feature
    y1 = data["Shelter 1"] ## Keeping only the Y feature
    x1_train, x1_test, y1_train, y1_test = train_test_split(x1, y1, test_size=0.3, random_state=0)
    
    return x1_train, x1_test, y1_train, y1_test

### Logistic Regression
def logreg_shelter1():
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

    data = generate_xy_shelter1()

    fitted = logreg1.fit(data[0], data[2])
    # shelter1result = logreg1.fit(data[0], data[2])
    y1_pred = fitted.predict(data[1])
    # accuracy = 'Accuracy of logistic regression classifier on Shelter 1 test set: {:.2f}'.format(logreg1.score(data[1], data[3]))
    
    ## Getting the probability value out for each of the test customers
    y1_pred_prob = fitted.predict_proba(data[2])
    
    return y1_pred_prob

def test_logreg():
    y1_pred_prob = logreg_shelter1()
    data = generate_xy_shelter1()
    shelter1data = csv_cleaner("donor_data.csv")

    ### Creating a test data for checking our results
    testData = shelter1data.loc[data[3]]
    testData["Probability"] = 0.0

    testData.Probability = y1_pred_prob

    return testData

# `The probability values you see on the right most column is the p-value associated with donation based on the data you created.`
# `For a new customer that comes in, you just need to put in their values in the exact format as the test data you had.`

# `For the second use case: That is, finding the the list of customers the process is exactly same as above. Have the list ready, and get the probabities out for these customers. Then finally sort it by their probabilities. The top 5 are teh ones with highest likelihood'`
def topfive():
    testData = test_logreg()
    testData = testData.sort_values(["Probability"],ascending=False)
    top5 = testData.head(5)

    return top5

topfive()
# `The list above is the top 5 customers with highest likelihood of donation.` 
# `The model can be improved using hyperparameter tuning, or using some other classifier, like Random Forest.`