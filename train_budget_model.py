import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
import joblib

# Load the dataset
data = pd.read_csv('family_budget.csv')  # Assuming the file is in the same directory as the script

# Prepare the data for training
# Select relevant features
X = data[['income', 'family_size', 'location']]  # Use multiple features including income, family size, and location
y = data[['rent', 'groceries', 'transport', 'utilities', 'entertainment', 'healthcare']].sum(axis=1)  # Total expenses

# Encode categorical features
# OneHotEncode the 'location' feature
preprocessor = ColumnTransformer(
    transformers=[
        ('loc', OneHotEncoder(), ['location'])
    ],
    remainder='passthrough'  # Leave other columns as is
)

# Create a pipeline that first transforms data and then applies linear regression
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
pipeline.fit(X_train, y_train)

# Save the model to a file
joblib.dump(pipeline, 'budget_model.pkl')  # Save the model in the same directory as the script
print("Model trained and saved as 'budget_model.pkl'")
