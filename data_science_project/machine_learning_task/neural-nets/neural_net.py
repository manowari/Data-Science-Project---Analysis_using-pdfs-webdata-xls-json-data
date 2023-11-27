import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, classification_report, mean_squared_error
from sklearn.preprocessing import StandardScaler
from tensorflow import keras
from tensorflow.keras import layers

# Assuming 'df' is your DataFrame with features and target variable
# X contains your features (e.g., scores, possession)
# y is your target variable (e.g., game outcome)

# Extract features (X) and target variable (y) from the DataFrame
X = df.drop(columns=['target_variable_column'])
y = df['target_variable_column']

# Perform train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Logistic Regression
logistic_model = LogisticRegression()
logistic_model.fit(X_train, y_train)
logistic_predictions = logistic_model.predict(X_test)

# Evaluate Logistic Regression
accuracy_logistic = accuracy_score(y_test, logistic_predictions)
classification_report_logistic = classification_report(y_test, logistic_predictions)

print("Logistic Regression Accuracy:", accuracy_logistic)
print("Logistic Regression Classification Report:\n", classification_report_logistic)

# Linear Regression
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)
linear_predictions = linear_model.predict(X_test)

# Evaluate Linear Regression
mse_linear = mean_squared_error(y_test, linear_predictions)
print("Linear Regression Mean Squared Error:", mse_linear)

# Neural Network
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    layers.Dense(1)  # Assuming a regression task, so only one output neuron
])

model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(X_train_scaled, y_train, epochs=50, batch_size=32, validation_split=0.2)

neural_predictions = model.predict(X_test_scaled)
mse_neural = mean_squared_error(y_test, neural_predictions)
print("Neural Network Mean Squared Error:", mse_neural)
