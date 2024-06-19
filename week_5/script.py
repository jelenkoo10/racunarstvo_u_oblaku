import subprocess

# Install required packages
subprocess.check_call(["pip", "install", "numpy", "pandas", "scikit-learn", "matplotlib", "seaborn"])

# Now import the required libraries
import numpy as np 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Read the dataset
dataset = pd.read_csv("HousingData.csv")
df = pd.DataFrame(dataset)

# Drop N/A values
df.dropna(inplace=True)

# Drop duplicates
df.drop_duplicates(inplace=True)

# Prepare data for training
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# Feature scaling
mm = MinMaxScaler()
X_train = mm.fit_transform(X_train)
X_test = mm.transform(X_test)

# Train RandomForestRegressor
forestModel = RandomForestRegressor()
forestModel.fit(X_train, y_train)

# Make predictions
predictions = forestModel.predict(X_test)

# Evaluation model
rmse = mean_squared_error(y_test, predictions)
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print(f"Root Mean Squared Error (RMSE): {rmse}")
print(f"Mean Absolute Error (MAE): {mae}")
print(f"R-squared (R2): {r2}")
