import pandas as pd
import numpy as np
from sklearn.externals import joblib
from sklearn.linear_model import LinearRegression

# load dataset
dataset = pd.read_csv(
    '/Users/miketondu/Dropbox/Data Science/Sharpest Minds/odds_data/bolivian_football_odds_prepared.csv',
    parse_dates=['date'])

dataset = dataset.loc[:, ['home_team', 'away_team', 'altitude',
                          'home_odds', 'draw_odds', 'away_odds',
                          'home_win']         # Target variable
          ]
dataset.dropna(inplace=True)
print(dataset.home_team.unique())

# Separate features and targe
X = dataset.iloc[:, :-1]
X = pd.get_dummies(X)
y = dataset.iloc[:, -1]

# Fit model
lr = LinearRegression()
lr.fit(X, y)

# Save your model
joblib.dump(lr, 'model.pkl')
print("Model dumped!")

# Load the model that you just saved
lr = joblib.load('model.pkl')

# Saving the data columns from training
model_columns = list(X.columns)
joblib.dump(model_columns, 'model_columns.pkl')
print("Models columns dumped!")
print(model_columns)
