# -*- coding: utf-8 -*-
"""KaggleTest.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1etRUepXpBcZnCsly9pp2av99LFci3V7Y
"""

pip install pandas scikit-learn matplotlib

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

#Load Dataset

df = pd.read_csv('/content/kaggle_survey_2022_responses.csv')

# Step 4: Exclude the Second Row

df = df.drop(1)
df = df.reset_index(drop=True)

# select columns

X = df[['Q11', 'Q30', 'Q27', 'Q26', 'Q23']]
Y = df['Q29']

# Step 7: Convert Categorical Data

X_encoded = pd.get_dummies(X)
Y_encoded = pd.get_dummies(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X_encoded, Y_encoded, test_size=0.2, random_state=42)

model = RandomForestRegressor()
model.fit(X_train, Y_train)

predictions = model.predict(X_test)
mse = mean_squared_error(Y_test, predictions)
print(f'Mean Squared Error: {mse}')

plt.scatter(Y_test, predictions)
plt.xlabel('Actual Salary')
plt.ylabel('Predicted Salary')
plt.title('Actual vs. Predicted Salary')
plt.show()

echo "# final458" >> README.md
  git init
  git add README.md
  git commit -m "first commit"
  git branch -M main
  git remote add origin https://github.com/courtney-k/final458.git
  git push -u origin main