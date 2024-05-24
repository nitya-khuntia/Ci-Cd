import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, f1_score
import joblib

# Load the dataset
dataset_path = 'insurance_data_cleaned.csv'  # Update the path if necessary
data = pd.read_csv(dataset_path)

# Preparing the target variable and features
y = data['Claim Approved']
# Include 'claim' in the features
X = data.drop(['index', 'PatientID', 'Claim Approved'], axis=1)

# Defining preprocessing for numerical features including 'claim'
numeric_features = ['age', 'bmi', 'bloodpressure', 'children', 'claim']
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())])

# Defining preprocessing for categorical features
categorical_features = ['gender', 'diabetic', 'smoker', 'region']
categorical_transformer = OneHotEncoder(handle_unknown='ignore')

# Combining preprocessing steps
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)])

# Create the preprocessing and modeling pipeline
pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                           ('classifier', RandomForestClassifier())])

# Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training the model
pipeline.fit(X_train, y_train)

# Predictions
y_pred = pipeline.predict(X_test)

# Evaluation
accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred, pos_label='Yes')

print(f'Accuracy: {accuracy}')
print(f'F1 Score: {f1}')

# Save the model and preprocessing pipeline
joblib.dump(pipeline, 'insurance_claim_pipeline.joblib')
