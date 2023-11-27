import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Assuming 'df' is your DataFrame with features and target variable
# Replace 'target_variable_column' with the actual column name

# Extract features (X) and target variable (y) from the DataFrame
X = df.drop(columns=['target_variable_column'])
y = df['target_variable_column']

# Perform train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Logistic Regression model
logistic_model = LogisticRegression()

# Train the model
logistic_model.fit(X_train, y_train)

# Make predictions on the test set
predictions = logistic_model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, predictions)
classification_report_result = classification_report(y_test, predictions)

# Print evaluation metrics
print(f"Accuracy: {accuracy:.2f}")
print("Classification Report:\n", classification_report_result)
