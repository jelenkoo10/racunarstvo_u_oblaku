import sys
import numpy as np
import pandas as pd

input_file_path = sys.argv[1]

# Read the dataset
dataset = pd.read_csv(input_file_path)
df = pd.DataFrame(dataset)

# Drop N/A values
df.dropna(inplace=True)

# Drop duplicates
df.drop_duplicates(inplace=True)

df.to_csv('output.csv', index=False)

