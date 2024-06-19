import sys
import numpy as np
import pandas as pd
from sklearn.model_selection import KFold
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

input_file_path = sys.argv[1]
n_splits = int(sys.argv[2])  # The total number of folds
current_fold = int(sys.argv[3])  # The current fold to process

# Load preprocessed dataset
df = pd.read_csv(input_file_path)

# Prepare data for training
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

# Initialize KFold
kf = KFold(n_splits=n_splits, shuffle=True, random_state=1)

# Initialize variables for slicing folds
fold_idx = 0

for train_index, test_index in kf.split(X):
    fold_idx += 1
    if fold_idx != current_fold:
        continue

    # Slicing the dataset for the current fold
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

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
    break 

