import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

def train_and_evaluate_model(cleaned_dataset):
    data = pd.read_csv(cleaned_dataset)
    
    X = data.drop(columns=['MEDV'])
    y = data['MEDV']
    
    model = KNeighborsRegressor()
    model.fit(X, y)
    
    y_pred = model.predict(X)
    rmse = mean_squared_error(y, y_pred, squared=False)
    mean_y = y.mean()
    prmse = (rmse / mean_y) * 100
    
    return rmse, prmse

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Train and evaluate regression model')
    parser.add_argument('--cleaned_dataset', type=str, help='Path to the cleaned dataset CSV file')
    args = parser.parse_args()
    
    performance_metrics = train_and_evaluate_model(args.cleaned_dataset)
    print("(RMSE, PRMSE):", performance_metrics)
