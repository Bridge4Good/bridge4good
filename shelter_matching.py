# ## This code below, will help identify who the top potential donors are for any given shelter. This can be used by the shelters for targetting email campaigns

import pandas as pd
import numpy as np

from sklearn import preprocessing
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.model_selection import GridSearchCV

# ## Shelter 1 Model - Train and test with shelter1.csv data
shelter1data = pd.read_csv("Shelter1_data.csv",header=0)
shelter1data["Shelter 1"] = np.random.randint(0, 2, shelter1data.shape[0])

### Loading the data here (reusing the code)
#shelter1data = pd.read_csv('.\donors.csv',header=0)
shelter1data_RAW = shelter1data.copy()
shelter1data = shelter1data.dropna()

### To effectively capture the effect of city and state , you need to one-hot-encode it. That is convert the state/city column to a binary variable
shelter1data = pd.get_dummies(shelter1data, columns = ["Donor City", "Donor State"])

### Removing Zip as this is redundant information, unless you are capturing the distance between the shelter and the customer using this. 
shelter1data = shelter1data.iloc[:,2:]

x1 = shelter1data.drop(["Shelter 1"], axis = 1) ## Keeping all except the Y feature
y1 = shelter1data["Shelter 1"] ## Keeping only the Y feature

### Logistic Regression

x1_train, x1_test, y1_train, y1_test = train_test_split(x1, y1, test_size=0.3, random_state=0)
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

shelter1result = logreg1.fit(x1_train, y1_train)
print(shelter1result)

y1_pred = logreg1.predict(x1_test)
print('Accuracy of logistic regression classifier on Shelter 1 test set: {:.2f}'.format(logreg1.score(x1_test, y1_test)))

## Getting the probability value out for each of the test customers
y1_pred_prob = logreg1.predict_proba(x1_test)

### Creating a test data for checking our results
testData = shelter1data_RAW.loc[y1_test]
testData["Probability"] = 0.0

testData.Probability = y1_pred_prob

print(testData)

# `The probability values you see on teh right most column is the p-value associated with donation based on the data you created.`
# `For a new customer that comes in, you just need to put in their values in the exact format as the test data you had.`

shelter1data.columns

# `For the second use case: That is, finding the the list of customers teh process is exactly same as above. Have the list ready, and get the probabities out for these customers. Then finally sort it by their probabilities. The top 5 are teh ones with highest likelihood'`
testData = testData.sort_values(["Probability"],ascending=False)
print(testData.head(5))

# `The list above is the top 5 customers with highest likelihood of donation.` 
# `The model can be improved using hyperparameter tuning, or using some other classifier, like Random Forest.`
