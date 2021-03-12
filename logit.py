# Logistic regression

# Load modules
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report

# Load dataset
df = pd.read_pickle("data/df.pkl")

df2 = pd.get_dummies(df, drop_first=True)
df2

X = df2[['Age', 'Education', 'Income', 'Profile', 'Sex_Woman']]
y = df2['Consumption_Yes']


# all parameters not specified are set to their defaults
model = LogisticRegression()

# Fit model
model.fit(X, y)

model.coef_
model.classes_

model.score(X, y)

confusion_matrix(y, model.predict(X))

print(classification_report(y, model.predict(X)))