import pandas as pd
from sklearn.model_selection import train_test_split
import pytest

# Sample data (replace with actual data structure if needed)
data = pd.DataFrame({'age': [39, 24, 38],
                   'bmi': [23.3, 30.1, 33.3],
                   'bloodpressure': [91, 87, 82],
                   'children': [0, 0, 0],
                   'claim': [1121.87, 1131.51, 1135.94],
                   'gender': ['male', 'male', 'male'],
                   'diabetic': ['Yes', 'No', 'Yes'],
                   'smoker': ['No', 'No', 'No'],
                   'region': ['southeast', 'southeast', 'southeast'],
                   'Claim Approved': ['Yes', 'Yes', 'Yes']})


# Test data loading 
def test_data_loading():
  loaded_data = pd.read_csv('insurance_data_cleaned.csv')  # Replace with actual path if needed
  # Assert the number of rows and columns
  assert loaded_data.shape[0] == 1340 
  assert loaded_data.shape[1] == 12

#Testing features and target variable separation
def test_feature_target_separation():
  y = data['Claim Approved']
  X = data.drop(['Claim Approved'], axis=1)
  assert X.shape[1] == len(data.columns) - 1  # Assert feature count matches
  assert (y == data['Claim Approved']).all()  # Assert target variable matches

#Testing Feature Definitions
def test_feature_definitions():
  numeric_features = ['age', 'bmi', 'bloodpressure', 'children', 'claim']
  categorical_features = ['gender', 'diabetic', 'smoker', 'region']
  assert numeric_features == ['age', 'bmi', 'bloodpressure', 'children', 'claim']
  assert categorical_features == ['gender', 'diabetic', 'smoker', 'region']

