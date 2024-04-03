import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error
import numpy as np

def train_and_evaluate_model(cleaned_dataset, target_column, kFold):
    data = pd.read_csv(cleaned_dataset)
    X = data.drop(columns=[target_column])
    y = data[target_column]

    kf = KFold(n_splits=kFold)

    rmseArray = []
    prmseArray = []
    for train_index, test_index in kf.split(X):
        X_train, X_test = X.iloc[train_index], X.iloc[test_index]
        y_train, y_test = y.iloc[train_index], y.iloc[test_index]

        model = KNeighborsRegressor()
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        mean_y = y_test.mean()
        prmse = (rmse / mean_y) * 100

        rmseArray.append(rmse)
        prmseArray.append(prmse)

    avg_rmse = np.mean(rmseArray)
    avg_prmse = np.mean(prmseArray)

    return avg_rmse, avg_prmse

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Train and evaluate regression model using k-fold cross validation')
    parser.add_argument('--cleaned_dataset', type=str, help='Path to the cleaned dataset CSV file')
    parser.add_argument('--target_column', type=str, help='Name of the target column')
    parser.add_argument('--kFold', type=int, help='Number of folds for cross validation')
    args = parser.parse_args()
    
    performance_metrics = train_and_evaluate_model(args.cleaned_dataset, args.target_column, args.kFold)
    print("(Average RMSE, average PRMSE):", performance_metrics)
