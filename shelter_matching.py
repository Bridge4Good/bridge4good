import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt

from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import seaborn as sns
from sklearn.model_selection import GridSearchCV

sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)

# ## Shelter 1 Model - Train and test with shelter1.csv data

### Loading the data here (reusing the code)
shelter1data = pd.read_csv('Shelter1_donor.csv',header=0)
shelter1data_RAW = shelter1data.copy()
shelter1data = shelter1data.dropna()

# print(shelter1data.head())

### To effectively capture the effect of city and state , you need to one-hot-encode it. That is convert the state/city column to a binary variable
# shelter1data = pd.get_dummies(shelter1data, columns = ["Donor City", "Donor State"])


### Removing Zip as this is redundant information, unless you are capturing the distance between the shelter and the customer using this. 
#### (Add that variable if you can, will be a much better for your storyline)
# shelter1data = shelter1data.iloc[:,2:]
# print(shelter1data.shape)

# Now you have 90 rows and 118 columns. Get the final X & y out now.
print(shelter1data.head())

x = shelter1data.iloc[:, 0:2].values
y = shelter1data.iloc[:, 2].values

# ### Logistic Regression

x1_train, x1_test, y1_train, y1_test = train_test_split(x, y, test_size=0.3, random_state=0)
logreg1 = LogisticRegression(penalty='l2',
    dual=False,
    tol=0.0001,
    C=1.0,
    fit_intercept=True,
    intercept_scaling=1,
    class_weight=None,
    warm_start=False,
    n_jobs=-1,
    l1_ratio=None)

shelter1result = logreg1.fit(x1_train, y1_train)
print(shelter1result)

y1_pred = logreg1.predict(x1_test)
print(logreg1.score(x1_test), y1_test)

# print('Accuracy of logistic regression classifier on Shelter 1 test set: {:.2f}'.format(logreg1.score(x1_test, y1_test)))

## Getting the probability value out for each of the test customers
y1_pred_prob = logreg1.predict_proba(x1_test)

### Creating a test data for checking our results
testData = shelter1data_RAW.loc[y1_test.index]
testData["Probability"] = 0.0

testData.Probability = y1_pred_prob

print(testData)

# `The probability values you see on teh right most column is the p-value associated with donation based on the data you created.`
# `For a new customer that comes in, you just need to put in their values in the exact format as the test data you had. That is, they should have these 118 columns:`

shelter1data.columns

# `For the second use case: That is, finding the the list of customers teh process is exactly same as above. Have the list ready, and get the probabities out for these customers. Then finally sort it by their probabilities. The top 5 are teh ones with highest likelihood'`
testData = testData.sort_values(["Probability"],ascending=False)
testData.head(5)

# `The list above is the top 5 customers with highest likelihood of donation.` 
# `Again, the model has a lot of scope of imporvement: you can try something called GridSearch for hyperparameter tuning. Also try out soem otehr classifier, like Random Forrest maybe. They'll give you good results.`

# `Repeat the steps above for the other three shelters`
