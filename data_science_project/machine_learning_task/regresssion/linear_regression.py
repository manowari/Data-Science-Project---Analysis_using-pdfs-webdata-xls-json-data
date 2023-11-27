import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Assuming 'df' is your DataFrame with features and target variable
# Replace 'target_variable_column' with the actual column name

# Extract features (X) and target variable (y) from the DataFrame
X = df.drop(columns=['target_variable_column'])
y = df['target_variable_column']

# Perform train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Linear Regression model
linear_model = LinearRegression()

# Train the model
linear_model.fit(X_train, y_train)

# Make predictions on the test set
predictions = linear_model.predict(X_test)
