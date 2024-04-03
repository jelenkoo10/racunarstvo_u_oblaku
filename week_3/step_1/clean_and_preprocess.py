import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

def clean_and_preprocess(dataset_file, target_column, train_percentage):
    print("Received arguments:")
    print("dataset_file:", dataset_file)
    print("target_column:", target_column)
    print("train_percentage:", train_percentage)

    data = pd.read_csv(dataset_file)
    
    data = data.dropna()
         
    X = data.drop(columns=[target_column])
    y = data[target_column]
    
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)
    
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=1-train_percentage, random_state=42)
    
    cleaned_data = np.column_stack((X_train, y_train))
    cleaned_data = pd.DataFrame(cleaned_data, columns=list(X.columns) + [target_column])
    cleaned_data.to_csv("./cleaned_dataset.csv", index=False)

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Clean and preprocess dataset')
    parser.add_argument('--dataset', type=str, help='Path to the dataset CSV file')
    parser.add_argument('--target', type=str, help='Name of the target column')
    parser.add_argument('--train_percentage', type=float, help='Percentage of data to be used for training')
    args = parser.parse_args()
    
    clean_and_preprocess(args.dataset)
